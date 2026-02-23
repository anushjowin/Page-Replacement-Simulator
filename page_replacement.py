#--FIFO--
def fifo(reference_string, frames):
    memory = []
    page_faults = 0
    states = []

    for page in reference_string:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
            page_faults += 1

        states.append(memory.copy())

    return states, page_faults

def lru(reference_string, frames):
    memory = []
    page_faults = 0
    states = []
    recent_use = []

    for page in reference_string:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                lru_page = recent_use.pop(0)
                memory.remove(lru_page)
                memory.append(page)
            page_faults += 1
        else:
            recent_use.remove(page)

        recent_use.append(page)
        states.append(memory.copy())

    return states, page_faults

def optimal(reference_string, frames):
    memory = []
    page_faults = 0
    states = []

    for i in range(len(reference_string)):
        page = reference_string[i]

        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                future = reference_string[i+1:]
                replace_page = None
                farthest = -1

                for m in memory:
                    if m not in future:
                        replace_page = m
                        break
                    else:
                        index = future.index(m)
                        if index > farthest:
                            farthest = index
                            replace_page = m

                memory.remove(replace_page)
                memory.append(page)

            page_faults += 1

        states.append(memory.copy())

    return states, page_faults



# ---- Testing Section ----

reference_string = list(map(int, input("Enter reference string (space separated): ").split()))
frames = int(input("Enter number of frames: "))

print("\nChoose Algorithm:")
print("1. FIFO")
print("2. LRU")
print("3. Optimal")

choice = int(input("Enter choice: "))

if choice == 1:
    states, faults = fifo(reference_string, frames)
    print("\nFIFO Simulation:\n")
elif choice == 2:
    states, faults = lru(reference_string, frames)
    print("\nLRU Simulation:\n")
elif choice == 3:
    states, faults = optimal(reference_string, frames)
    print("\nOptimal Simulation:\n")
else:
    print("Invalid choice!")
    exit()


for i, state in enumerate(states):
    print(f"Step {i+1}: {state}")

print("\nTotal Page Faults:", faults)



