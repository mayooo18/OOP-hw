TEST_WEIGHT = 0.30
EXAM_WEIGHT = 0.30
DISCUSSION_WEIGHT = 0.20
PROJECT_WEIGHT = 0.20



def avg_subjects(scores):
    numbers = [float(x) for x in scores if x.strip() != ""]
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

def weight_final(testavg, examavg, discussionavg, projectavg):
    return (testavg * TEST_WEIGHT +
            examavg * EXAM_WEIGHT +
            discussionavg * DISCUSSION_WEIGHT +
            projectavg * PROJECT_WEIGHT)

def analyze_grades(final_scores):
    buckets = {
        "90+": 0,
        "80-89": 0,
        "70-79": 0,
        "60-69": 0,
        "<60": 0
    }
    for score in final_scores:
        if score >= 90:
            buckets["90+"] += 1
        elif score >= 80:
            buckets["80-89"] += 1
        elif score >= 70:
            buckets["70-79"] += 1
        elif score >= 60:
            buckets["60-69"] += 1
        else:
            buckets["<60"] += 1

    print("\nGrade Distribution:")
    for k, v in buckets.items():
        print(f"{k}: {v} students")

def main():
    filename = input("Enter the filename containing student grades (.csv): ").strip()
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()

        if not lines:
            print("Error: file is empty.")
            return

        header = lines[0].strip().split(",")
        final_scores = []

        for line in lines[1:]:
            if not line.strip():
                continue
            parts = line.strip().split(",")
            if len(parts) < 10:
                continue

            name = parts[0]
            student_id = parts[1]
            tests = parts[2:5]
            exams = parts[5:7]
            discussions = parts[7:9]

            try:
                project = float(parts[9])
            except ValueError:
                project = 0.0

            test_avg = avg_subjects(tests)
            exam_avg = avg_subjects(exams)
            discussion_avg = avg_subjects(discussions)
            final_score = weight_final(test_avg, exam_avg, discussion_avg, project)
            final_scores.append(final_score)

            print(f"{name} ({student_id}): {final_score:.2f}")

        if final_scores:
            analyze_grades(final_scores)
        else:
            print("No valid student rows found.")

    except FileNotFoundError:
        print("Error: File not found")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
