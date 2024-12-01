'''
    Pre: Se espera un argumento 'coins' que contenga numeros de la siguiente forma:
            [w,x,y,...,z]
        
    Pos: Devuelve un numero que indica el maximo valor acumulabe por sofia y un 
        array 'steps' que indica que movimiento hizo cada jugador.
'''
def max_coins(coins):
    
    n = len(coins)
    dp = [[0] * n for _ in range(n)]

    # length es el núero de monedas en el rango
    for length in range(1, n +1):

        for i in range(n - length + 1):

            j = i + length - 1 # El final del rango es i + length- 1

            if i == j : # Solo una moneda
                dp[i][j] = coins[i]

            elif i == j-1:
                dp[i][j] = max(coins[i],coins[j])

            else:

                if coins[i+1]>coins[j]:
                    pick_i = coins[i] + dp[i+2][j]

                else:
                    pick_i = coins[i] + dp[i+1][j-1]

                if coins[j-1]>coins[i]:
                    pick_j = coins[j] + dp[i][j-2]

                else:
                    pick_j = coins[j] + dp[i+1][j-1]
                dp[i][j] = max(pick_i, pick_j)
            
            # Guardar el paso que ocurrio ¿Como guardo que moneda agarro Mateo?
            # Para sofia seria steps.append(dp[i][j])

    # La ganancia de Sophia es: dp[0][n-1]
    # La ganancia de mateo es: sum(coins) - dp[i][j]
    return dp[0][n-1], abs(sum(coins) - dp[0][n-1]), reconstruct_steps(coins, dp)


def reconstruct_steps(coins, dp):
    steps = []
    i, j = 0, len(coins) - 1
    turn = 'Sofia'

    while i <= j:
        if i == j:
            steps.append(f"{turn} agarra la moneda ({coins[i]})")
            break

        if coins[i + 1] > coins[j]:
            if dp[i][j] == coins[i] + dp[i + 2][j]:
                steps.append(f"{turn} agarra la moneda ({coins[i]})")
                i += 1
            else:
                steps.append(f"{turn} agarra la moneda ({coins[j]})")
                j -= 1
        else:
            if dp[i][j] == coins[j] + dp[i][j - 2]:
                steps.append(f"{turn} agarra la moneda ({coins[j]})")
                j -= 1
            else:
                steps.append(f"{turn} agarra la moneda ({coins[i]})")
                i += 1

        turn = 'Mateo' if turn == 'Sofia' else 'Sofia'

    return steps