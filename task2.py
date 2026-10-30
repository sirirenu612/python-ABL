
# Student Email and Identifier Validation

def validate_email(email):
    errors = []

    # Check missing email
    if email == "":
        errors.append("Missing email address")
        return errors

    # Check spaces
    if " " in email:
        errors.append("Spaces are not allowed")

    # Check @ symbol
    if email.count("@") == 0:
        errors.append("Missing @ symbol")
        return errors

    if email.count("@") > 1:
        errors.append("Malformed separator: multiple @ symbols")
        return errors

    parts = email.split("@")
    username = parts[0]
    domain = parts[1]

    # Check missing components
    if username == "":
        errors.append("Missing username")

    if domain == "":
        errors.append("Missing domain")
        return errors

    # Check username characters
    allowed_username = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789._-"
    )

    for ch in username:
        if ch not in allowed_username:
            errors.append("Invalid character in username")
            break

    # Check username separators
    if username.startswith(".") or username.endswith("."):
        errors.append("Malformed username separator")

    if ".." in username:
        errors.append("Consecutive dots in username")

    # Check domain components
    domain_parts = domain.split(".")

    if len(domain_parts) < 2:
        errors.append("Missing domain extension")

    for part in domain_parts:
        if part == "":
            errors.append("Missing domain component")
            break

    # Check domain characters
    allowed_domain = (
        "abcdefghijklmnopqrstuvwxyz"
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        "0123456789-."
    )

    for ch in domain:
        if ch not in allowed_domain:
            errors.append("Invalid character in domain")
            break

    # Check domain labels and extension
    for part in domain_parts:
        if part.startswith("-") or part.endswith("-"):
            errors.append("Malformed domain separator")
            break

    if domain_parts[-1] != "" and not domain_parts[-1].isalpha():
        errors.append("Domain extension must contain letters only")

    return errors


def validate_id(reg_id):
    errors = []

    if reg_id == "":
        errors.append("Missing registration identifier")
        return errors

    # Check separator positions
    if reg_id.startswith("-") or reg_id.endswith("-") or "--" in reg_id:
        errors.append("Malformed hyphen separators")

    parts = reg_id.split("-")

    if len(parts) != 3:
        errors.append("Identifier must have three components")
        return errors

    course = parts[0]
    year = parts[1]
    number = parts[2]

    # Check missing components
    if course == "":
        errors.append("Missing course code")

    if year == "":
        errors.append("Missing year")

    if number == "":
        errors.append("Missing student number")

    # Check course code
    if course != "" and course != "BTECH":
        errors.append("Invalid course code; expected BTECH")

    # Check year
    if year != "" and (len(year) != 4 or not year.isdigit()):
        errors.append("Year must contain four digits")

    # Check student number
    if number != "" and (len(number) != 3 or not number.isdigit()):
        errors.append("Student number must contain three digits")

    return errors

# Main program
email = input("Enter student email: ")
reg_id = input("Enter registration ID: ")

email_errors = validate_email(email)
id_errors = validate_id(reg_id)

print("\n--- Email Validation ---")

if len(email_errors) == 0:
    print("Email is valid.")
else:
    print("Email is invalid.")
    for error in email_errors:
        print("-", error)

print("\n--- Registration ID Validation ---")

if len(id_errors) == 0:
    print("Registration ID is valid.")
else:
    print("Registration ID is invalid.")
    for error in id_errors:
        print("-", error)
