data: [str] = []


with open("./data", 'r') as file:
    [data.append(c.rstrip()) for c in file]


# Part 1
gamma_rate: str = ''
epsilon_rate: str = ''
true_occurences: int = 0
false_occurences: int = 0
for i in range(len(data[0])):
    true_occurences = 0
    false_occurences = 0
    for d in data:
        if d[i] == '0':
            false_occurences += 1
        else:
            true_occurences += 1
    gamma_rate += '1' if true_occurences > false_occurences else '0'
    epsilon_rate += '1' if true_occurences < false_occurences else '0'

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
# Part 2
oxygen_generator_rating_filtered = data.copy()
co2_scrubber_rating_filtered = data.copy()
true_occ_oxygen: int = 0
false_occ_oxygen: int = 0
true_occ_co2: int = 0
false_occ_co2: int = 0
def discard_bit_criteria(data: [str], c: str, index: int)-> [str]:
    new_data: [str] = []
    # checks data matches c at index for each element
    for d in data:
        if d[index] == c:
            new_data.append(d)
    return new_data

for i in range(len(data[0])):
    true_occ_oxygen = 0
    false_occ_oxygen = 0
    true_occ_co2 = 0
    false_occ_co2 = 0
    if len(oxygen_generator_rating_filtered) > 1:
        for d in oxygen_generator_rating_filtered:
            if d[i] == '0':
                false_occ_oxygen += 1
            else:
                true_occ_oxygen += 1
        oxygen_generator_rating_filtered = discard_bit_criteria(
            oxygen_generator_rating_filtered,
            '1' if true_occ_oxygen >= false_occ_oxygen else '0',
            i
        )
    if len(co2_scrubber_rating_filtered) > 1:
        for d in co2_scrubber_rating_filtered:
            if d[i] == '0':
                false_occ_co2 += 1
            else:
                true_occ_co2 += 1
        co2_scrubber_rating_filtered = discard_bit_criteria(
            co2_scrubber_rating_filtered,
            '1' if true_occ_co2 < false_occ_co2 else '0',
            i
        )

print(int(co2_scrubber_rating_filtered[0], 2) * int(oxygen_generator_rating_filtered[0], 2))
