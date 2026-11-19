
# Practical Work 11 — Variant A

Student: Kairatbek Shakirov

## Topic
Page Replacement Algorithms in Operating Systems

## Algorithms
- FIFO (First In, First Out)
- LRU (Least Recently Used)
- Optimal Page Replacement

## Results

| Algorithm | 3 Frames | 4 Frames |
|-----------|----------|----------|
| FIFO      | 11       | 10       |
| LRU       | 11       | 9        |
| Optimal   | 9        | 7        |

## Belady's Anomaly

FIFO with 3 frames: 9 page faults

FIFO with 4 frames: 10 page faults

Belady's anomaly was detected.

## Conclusion

Optimal showed the lowest number of page faults.
LRU performed better than FIFO with 4 frames.
FIFO can show Belady's anomaly.

## How to Run

python3 practice11.py

