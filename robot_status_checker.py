# ============================================
# Scale AI — Robot Fleet Status Checker
# Built by: Elis Sanchez
# Description: Checks if a robot passes or
# needs escalation based on accuracy score
# ============================================

# collect robot data from user
robot_id  = input("Enter robot ID: ")
accuracy  = float(input("Enter accuracy score: "))
is_online = input("Is the robot online? (yes/no): ")

# check if robot passes or needs escalation
if accuracy >= 90:
    print(f"✅ PASS | Robot: {robot_id} | Accuracy: {accuracy}% | Online: {is_online}")
else:
    print(f"⚠️ ESCALATE | Robot: {robot_id} | Accuracy: {accuracy}% | Online: {is_online}")
