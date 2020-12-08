data = [
    "Andromeda - Shrub",#0
    "Bellflower - Flower",#1
    "China Pink - Flower",#2
    "Daffodil - Flower",#3
    "Evening Primrose - Flower",#4
    "French Marigold - Flower",#5
    "Hydrangea - Shrub",#6
    "Iris - Flower",#7
    "Japanese Camellia - Shrub",#8
    "Lavender - Shrub",#9
    "Lilac- Shrub",#10
    "Magnolia - Shrub",#11
    "Peony - Shrub",#12
    "Queen Anne's Lace - Flower",#13
    "Red Hot Poker - Flower",#14
    "Snapdragon - Flower",#15
    "Sunflower - Flower",#16
    "Tiger Lily - Flower",#17
    "Witch Hazel - Shrub",#18
]

flowers = []
shrubs = []

# write your code here
for eachboy in data:
    if  eachboy.endswith('Flower'):
        flowers.append(eachboy)
    if eachboy.endswith('Shrub'):
        shrubs.append(eachboy)


print(flowers)
print(shrubs)