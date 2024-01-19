import time
from datetime import datetime

def inside_circle(x, y, R, a, b):
    return (x-a)**2 + (y-b)**2 <= R**2

def count_points_in_circle(x, y, R):
    count = 0
    for i in range(-R, R+1):
        for j in range(-R, R+1):
            if inside_circle(x, y, R**2, i, j):
                count += 1
    return count

def main():
    start_time = time.time()

    with open("PDF_6_5_4_intput.txt", "r") as f:
        R = int(f.readline().strip())
        x, y = map(int, f.readline().split())

    result = count_points_in_circle(x, y, R)

    with open("PDF_6_5_4_output.txt", "w") as f:
        f.write(datetime.now().strftime('%d.%m.%Y %H:%M') + '\n')
        f.write(str(result) + '\n')
        elapsed_time = time.time() - start_time
        f.write(f"Потраченное время: {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    main()
