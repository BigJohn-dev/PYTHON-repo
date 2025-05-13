# World Population growth

WORLD_POPULATION = 8200000000
ANNUAL_GROWTH_RATE = 0.01

#using compound growth rate P = P0 * (1 + r)^t

print('Years\tAnticipated World Population\tNumerical representation')

for i in range(1, 101):
	population = WORLD_POPULATION * (1 + ANNUAL_GROWTH_RATE) ** i
	print(f'{i:<4}\t{population:>22.0f}\t\t{population:>20.0f}')