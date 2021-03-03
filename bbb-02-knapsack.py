
# Question: Given a list of items with values and weights, as well as a max weight,
# find the maximum value you can generate from items where the sum of the weights is less than the max.

# items = {(w:1, v:6), (w:2, v:10), (w:3, v:12)}
# maxWeight = 5
# knapsack(items, maxWeight) = 22

# for each item
# add that in the bag if the weight is under max
#       then call the function with a list of added values and current weight
# return max if something was added

# otherwise return somekey that represents the items and the value

def knapsack(items, maxWeight):
    return knapsackTopDown(items, maxWeight, 0)

def knapsackTopDown(items, maxWeight, currentWeight):
    print(items)
    if len(items) == 1:
        if currentWeight +items[0]['w'] <= maxWeight:
            return currentWeight + items[0]['w']
        else:
            return currentWeight

    currentWeights = []
    for index, item in enumerate(items):
        updatedItems = items.copy()
        updatedItems.pop(index)
        updatedWeight = currentWeight - item['w']
        currentWeights.append(knapsackTopDown(updatedItems, maxWeight, updatedWeight))
    return max(currentWeights)

items = [{'w':1, 'v':6}, {'w':2, 'v':10}, {'w':3, 'v':12}]
maxWeight = 5
print(knapsack(items, maxWeight)) # 22
