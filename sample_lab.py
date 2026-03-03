vowel_count, consonant_count, space_count, other_count = 0, 0, 0, 0

with open('input_text.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        for word in line.split(" "):
            for ch in word:
                letter = ch.lower()
                
                if letter in 'aeiou':
                    vowel_count += 1   
                elif letter in 'qwrtypsdfghjklzxcvbnm':
                    consonant_count += 1
                else:
                    other_count += 1

            space_count += 1

total = vowel_count + consonant_count + space_count + other_count

with open('report.txt', 'w') as f:
    f.write(f"Vowel Percentage: {(vowel_count / total) * 100}\n")
    f.write(f"Consonant Percentage: {(consonant_count / total) * 100}\n")
    f.write(f"Space Percentage: {(space_count / total) * 100}\n")
    f.write(f"Other Percentage: {(other_count / total) * 100}\n")
    


                
                           