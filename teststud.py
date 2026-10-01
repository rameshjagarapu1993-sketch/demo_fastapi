from students import (
    get_all_students,
    get_student_by_id,
    calculate_student_status
)


print("All Students:")
print(get_all_students())


student = get_student_by_id(1)

print("\nStudent:")
print(student)


status = calculate_student_status(student)

print("\nStatus:")
print(status)

