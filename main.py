import numpy as np
import datapoints
import time
import person
import matplotlib.pyplot as plt


def main():
    people = []
    for i in range(15000):
        people.append(person.Person())

    while True:
        year_passed = int(input("How Many Years: "))
        start = time.time()
        for i in range(year_passed):
            for human in people:
                human.year()
            population = person.Person.population
            for x in range(int(0.014*population)):
                people.append(person.Person(0))
                if population > 500000:
                    break
        new_people = []

        for human in people:
            if not human.dead:
                new_people.append(human)
        people = new_people
        print(f'Population: {person.Person.population}')
        # by 10 years
        age_group = [0] * 13
        population_age = [0] * 13
        for human in people:
            if human.has_parkinson:
                age_group[human.age//10] += 1
            population_age[human.age//10] += 1
        print(f'Age Population: {population_age}')
        print(f'Parkinson By Age Group: Total {sum(age_group)} Distribution: {age_group}')

        plt.hist([x.age for x in people], [i*10 for i in range(len(population_age))], (0, 120), color='green',
                 histtype='bar', rwidth=0.8)
        plt.xlabel('Age')
        plt.ylabel('No. of people')
        plt.title('Population')
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.hist([x.age for x in people if x.has_parkinson], [i*10 for i in range(len(population_age))], (0, 120), color='red',
                 histtype='bar', rwidth=0.8)
        plt.xlabel('Age')
        # frequency label
        plt.ylabel('No. of people')
        # plot title
        plt.title("Has Parkinson's")

        # percent
        plt.subplot(1, 2, 2)
        plt.bar([i for i in range(len(population_age))],
                [0 if population_age[i] == 0 else age_group[i] / population_age[i] * 100 for i in range(len(population_age))],
                tick_label=[f'{i*10}-{i*10+10-1}' for i in range(len(population_age))],
                width=0.8, color='green')
        plt.xlabel('Age')
        plt.ylabel('Percent')
        plt.xticks(rotation="vertical")
        plt.title("Has Parkinson's Percentage")

        end = time.time()
        print(f'Time Taken: {(end - start) // 60} min(s) {(end - start) % 60} seconds')

        plt.show()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
