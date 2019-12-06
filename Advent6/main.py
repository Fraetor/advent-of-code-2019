input_file = open("input", "r")
orbit_data = [[orbiter.rstrip("\n") for orbiter in line.split(")")] for line in input_file.readlines()]
# print(orbit_data)


def num_orbits(current_orbit):
    com_distance = 1
    while current_orbit[0] != "COM":
        com_distance += 1
        current_orbit = search_suborbit(current_orbit[0])
    return com_distance


def search_suborbit(target):
    for suborbit in orbit_data:
        if target == suborbit[1]:
            return suborbit


total = 0
for orbit in orbit_data:
    total += num_orbits(orbit)

print("The total number of direct and indirect orbits is: {}".format(total))
