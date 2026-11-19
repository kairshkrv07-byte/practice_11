
# Practical Work 11 - Variant A
# Page Replacement Algorithms

def fifo(pages, frames_count):
    frames = []
    faults = 0
    pointer = 0

    for page in pages:
        if page not in frames:
            faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                frames[pointer] = page
                pointer = (pointer + 1) % frames_count

    return faults


def lru(pages, frames_count):
    frames = []
    last_used = {}
    faults = 0

    for i, page in enumerate(pages):
        if page not in frames:
            faults += 1
            if len(frames) < frames_count:
                frames.append(page)
            else:
                victim = min(frames, key=lambda p: last_used[p])
                frames[frames.index(victim)] = page

        last_used[page] = i

    return faults


def optimal(pages, frames_count):
    frames = []
    faults = 0

    for i, page in enumerate(pages):
        if page in frames:
            continue

        faults += 1

        if len(frames) < frames_count:
            frames.append(page)
        else:
            future = pages[i + 1:]

            victim = max(
                frames,
                key=lambda p: future.index(p)
                if p in future else float("inf")
            )

            frames[frames.index(victim)] = page

    return faults


# Reference string

# Student: Kairatbek Shakirov
# Generate page references from full name

full_name = "KAIRATBEK SHAKIROV"

pages = [ord(char) % 10 for char in full_name if char.isalpha()]

print("Student:", full_name)
print("Generated pages:", pages)


print("PRACTICAL WORK 11 - VARIANT A")
print("Page reference string:", pages)

print("\nAlgorithm | 3 Frames | 4 Frames")
print("--------------------------------")

for name, algorithm in [
    ("FIFO", fifo),
    ("LRU", lru),
    ("Optimal", optimal)
]:
    result3 = algorithm(pages, 3)
    result4 = algorithm(pages, 4)
    print(f"{name:9} | {result3:^8} | {result4:^8}")

# Belady's anomaly test
print("\nBELADY'S ANOMALY TEST")

belady_pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]

fifo3 = fifo(belady_pages, 3)
fifo4 = fifo(belady_pages, 4)

print("FIFO with 3 frames:", fifo3)
print("FIFO with 4 frames:", fifo4)

if fifo4 > fifo3:
    print("Belady's anomaly detected!")
else:
    print("No Belady's anomaly detected.")

