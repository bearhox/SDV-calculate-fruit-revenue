def calculate_profit(fruit_counts, base_prices, artisan_skill=False):
    preserves_jar_profit = 0
    dehydrator_profit = 0
    keg_profit = 0

    for fruit, count in fruit_counts.items():
    # Calculate profit for preserves jar
        preserves_jar_profit += (2 * base_prices[fruit] + 50) * count


    # Calculate profit for dehydrator
        dehydrator_profit += (7.5 * base_prices[fruit] + 25) * (count // 5)

    # Calculate profit for keg
        keg_profit += (3 * base_prices[fruit]) * count

    if artisan_skill:
        preserves_jar_profit *= 1.4
        dehydrator_profit *= 1.4
        keg_profit *= 1.4

    return preserves_jar_profit, dehydrator_profit, keg_profit

def calculate_processing_time(fruit_counts, num_preserves_jars=1, num_dehydrators=1, num_kegs=1):
    preserves_jar_time = 0
    dehydrator_time = 0
    keg_time = 0

    for fruit, count in fruit_counts.items():
        # Calculate time for preserves jar
        preserves_jar_time += ((count * 4000) // 1750) // num_preserves_jars

        # Calculate time for dehydrator
        dehydrator_time += (((count // 5) * 1750) // 1750) // num_dehydrators

        # Calculate time for keg
        keg_time += ((count * 10000) // 1750) // num_kegs

    return preserves_jar_time, dehydrator_time, keg_time

def main():
    # Base prices of fruits
    base_prices = {
        'Normal Cranberry': 75,
        'Silver Cranberry': 93,
        'Gold Cranberry': 112,
        'Purple Cranberry': 150,
        # Add more fruits if needed
    }

    fruit_names = list(base_prices.keys())

    # Ask user for input
    fruit_counts = {}
    for fruit in fruit_names:
        count = int(input(f"How many {fruit}s do you have? "))
        fruit_counts[fruit] = count

    print("\nSelect an option:")
    print("1. Sell all fruits")
    print("2. Process all fruits")
    print("3. Sell quality fruits + Process Normal ones")
    
    action = input("\nEnter the number of your choice: ")

    if action == '1':
        total_profit = sum(count * base_prices[fruit] for fruit, count in fruit_counts.items())
        print(f"\nTotal profit from selling all fruits: {total_profit}g")
        print(f"Total Profit in case you have Tiller (10% extra): {round(total_profit * 1.1)}g")


    elif action == '2':
        preserves_jar_count = int(input("\nHow many Preserves Jars do you have? "))
        dehydrator_count = int(input("How many Dehydrators do you have? "))
        keg_count = int(input("How many Kegs do you have?"))

        preserves_jar_time, dehydrator_time, keg_time = calculate_processing_time(fruit_counts, preserves_jar_count, dehydrator_count, keg_count)
        print(f"\nTime to process all fruits using {preserves_jar_count} Preserves Jars: {preserves_jar_time} days")
        print(f"Time to process all fruits using {dehydrator_count} Dehydrators: {dehydrator_time} days")
        print(f"Time to process all fruits using {keg_count} Kegs: {keg_time} days")

        preserves_jar_profit, dehydrator_profit, keg_profit = calculate_profit(fruit_counts, base_prices)
        print(f"\nProfit from processing all fruits using Preserves Jar: {round(preserves_jar_profit)}g")
        print(f"Profit from processing all fruits using Dehydrator: {round(dehydrator_profit)}g")
        print(f"Profit from processing all fruits using Keg: {round(keg_profit)}g")

        preserves_jar_profit_with_artisan, dehydrator_profit_with_artisan, keg_profit_with_artisan = calculate_profit(fruit_counts, base_prices, artisan_skill=True)
        print(f"\nProfit in case you have artisan (40% extra) using Preserves Jar: {round(preserves_jar_profit_with_artisan)}g")
        print(f"Profit in case you have artisan (40% extra) using Dehydrator: {round(dehydrator_profit_with_artisan)}g")
        print(f"Profit in case you have artisan (40% extra) using Keg: {round(keg_profit_with_artisan)}g")

    elif action == '3':
        quality_fruits = {fruit: count for fruit, count in fruit_counts.items() if fruit != fruit_names[0]}
        normal_fruit_count = fruit_counts.get(fruit_names[0], 0)

        quality_profit = sum(count * base_prices[fruit] for fruit, count in quality_fruits.items())
        print(f"\Profit from selling quality fruits: {quality_profit}g")
        quality_profit_with_tiller = round(quality_profit * 1.1)
        print(f"Profit in case you have Tiller (10% extra): {quality_profit_with_tiller}g")

        preserves_jar_profit = 0
        dehydrator_profit = 0
        keg_profit = 0
        preserves_jar_profit_with_artisan = 0
        dehydrator_profit_with_artisan = 0
        keg_profit_with_artisan = 0
        if normal_fruit_count > 0:
            preserves_jar_count = int(input("\nHow many Preserves Jars do you have? "))
            dehydrator_count = int(input("How many Dehydrators do you have? "))
            keg_count = int(input("How many Kegs do you have? "))

            preserves_jar_time, dehydrator_time, keg_count = calculate_processing_time(fruit_counts, preserves_jar_count, dehydrator_count, keg_count)       
            print(f"\nTime to process {fruit_names[0]}s using Preserves Jar: {preserves_jar_time} days")
            print(f"Time to process {fruit_names[0]}s using Dehydrator: {dehydrator_time} days")
            print(f"Time to process {fruit_names[0]}s using Keg: {keg_time} days")

            preserves_jar_profit, dehydrator_profit, keg_profit = calculate_profit({fruit_names[0]: normal_fruit_count}, base_prices)
            print(f"\nProfit from processing {fruit_names[0]}s using Preserves Jar: {round(preserves_jar_profit)}g")
            print(f"Profit from processing {fruit_names[0]}s using Dehydrator: {round(dehydrator_profit)}g")
            print(f"Profit from processing {fruit_names[0]}s using Keg: {round(keg_profit)}g")

            preserves_jar_profit_with_artisan, dehydrator_profit_with_artisan, keg_profit_with_artisan = calculate_profit({fruit_names[0]: normal_fruit_count}, base_prices, artisan_skill=True)
            print(f"\nProfit in case you have artisan (40% extra) when processing {fruit_names[0]}s using Preserves Jar: {round(preserves_jar_profit_with_artisan)}g")
            print(f"Profit in case you have artisan (40% extra) when processing {fruit_names[0]}s using Dehydrator: {round(dehydrator_profit_with_artisan)}g")
            print(f"Profit in case you have artisan (40% extra) when processing {fruit_names[0]}s using Keg: {round(keg_profit_with_artisan)}g")
        else:
            print(f"\nThere are no {fruit_names[0]}s to process")

        print(f"\nFinal Profits:")
        print(f"\nUsing Preserves Jars: {quality_profit + round(preserves_jar_profit)}g")
        print(f"Using Dehydrators: {quality_profit + round(dehydrator_profit)}g")
        print(f"Using Kegs: {quality_profit + round(keg_profit)}g")
        
        print(f"\nUsing Preserves Jars With Tiller (10% extra on crops): {quality_profit_with_tiller + round(preserves_jar_profit)}g")
        print(f"Using Dehydrators With Tiller (10% extra on crops): {quality_profit_with_tiller + round(dehydrator_profit)}g")
        print(f"Using Kegs With Tiller (10% extra on crops): {quality_profit_with_tiller + round(keg_profit)}g")
        
        print(f"\nUsing Preserves Jars With Artisan (40% extra on artisan goods): {quality_profit + round(preserves_jar_profit_with_artisan)}g")
        print(f"Using Dehydrators With Artisan (40% extra on artisan goods): {quality_profit + round(dehydrator_profit_with_artisan)}g")
        print(f"Using Kegs With Artisan (40% extra on artisan goods): {quality_profit + round(keg_profit_with_artisan)}g")
        
        print(f"\nUsing Preserves Jars With Tiller (10% extra on crops) AND With Artisan (40% extra on artisan goods): {quality_profit_with_tiller + round(preserves_jar_profit_with_artisan)}g")
        print(f"Using Dehydrators With Tiller (10% extra on crops) AND With Artisan (40% extra on artisan goods): {quality_profit_with_tiller + round(dehydrator_profit_with_artisan)}g")
        print(f"Using Kegs With Tiller (10% extra on crops) AND With Artisan (40% extra on artisan goods): {quality_profit_with_tiller + round(keg_profit_with_artisan)}g")
    else:
        print("\nInvalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()

