def generate_remark(marks, attendance):

    if marks >= 85 and attendance >= 75:
        return "Excellent Performance"

    elif marks >= 60 and attendance >= 60:
        return "Good Performance"

    elif marks >= 40:
        return "Needs Improvement"

    else:
        return "At Risk"