def load_inventory(user_id):
    inventory_folder = 'data/' + str(user_id)
    item_inventory_file = inventory_folder + '/item_inventory.csv'
    monster_inventory_file = inventory_folder + '/monster_inventory.csv'

    # Membuat folder jika belum ada
    if not os.path.exists(inventory_folder):
        os.makedirs(inventory_folder)
        return [], []

    # Memuat item_inventory
    items = []
    if os.path.exists(item_inventory_file):
        with open(item_inventory_file, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                items.append(row)

    # Memuat monster_inventory
    monsters = []
    if os.path.exists(monster_inventory_file):
        with open(monster_inventory_file, newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                monsters.append(row)

    return items, monsters

# Fungsi untuk menyimpan inventory ke dalam file CSV
def save_inventory(user_id, items, monsters):
    inventory_folder = 'data/' + str(user_id)
    item_inventory_file = inventory_folder + '/item_inventory.csv'
    monster_inventory_file = inventory_folder + '/monster_inventory.csv'

    # Membuat folder jika belum ada
    if not os.path.exists(inventory_folder):
        os.makedirs(inventory_folder)

    # Menyimpan item_inventory
    with open(item_inventory_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(items)

    # Menyimpan monster_inventory
    with open(monster_inventory_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(monsters)

# Fungsi utama inventory
def inventory_main(user_id, o_w_c_a_coin):
    items, monsters = load_inventory(user_id)

    while True:
        # Menampilkan inventory
        print(f"============ INVENTORY LIST (User ID: {user_id}) ============")
        print(f"Jumlah O.W.C.A. Coin-mu sekarang {o_w_c_a_coin}.")

        # Menampilkan monsters
        for index, monster in enumerate(monsters, start=1):
            print(f"{index}. Monster       (Name: {monster[0]}, Lvl: {monster[1]}, HP: {monster[2]})")

        # Menampilkan items
        for index, item in enumerate(items, start=len(monsters)+1):
            print(f"{index}. Potion        (Type: {item[0]}, Qty: {item[1]})")

        # Meminta input dari pengguna
        print("\nKetikkan id untuk menampilkan detail item:")
        print("Ketik 'KELUAR' untuk kembali ke menu utama")
        choice = input(">>> ")

        # Keluar dari inventory jika pengguna memilih 'KELUAR'
        if choice.upper() == 'KELUAR':
            break

        # Menampilkan detail item jika pengguna memilih nomor item
        try:
            index = int(choice)
            if 1 <= index <= len(monsters):
                monster = monsters[index - 1]
                print(f"Monster\nName      : {monster[0]}\nATK Power : {monster[1]}\nDEF Power : {monster[2]}\nHP        : {monster[3]}\nLevel     : {monster[4]}")
            elif len(monsters) + 1 <= index <= len(items) + len(monsters):
                item = items[index - len(monsters) - 1]
                print(f"Potion\nType      : {item[0]}\nQuantity  : {item[1]}")
            else:
                print("Input tidak valid, coba lagi.")
        except ValueError:
            print("Input tidak valid, coba lagi.")

if __name__ == "__main__":
    user_id = 1  # ID pengguna sementara
    o_w_c_a_coin = 900  # Jumlah O.W.C.A. Coin sementara
    inventory_main(user_id, o_w_c_a_coin)
