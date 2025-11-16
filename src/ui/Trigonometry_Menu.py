# Trigonometry Menu
from src.utils.input_utils import get_decimal_input
from src.utils.input_utils import get_choice_input
from src.utils.input_utils import smart_decimal_input
from src.utils.input_utils import get_letter_choice
from src.geometry import Trigonometry_Functions as trig



def run_trigonometry_menu():
    print(
        "Press 1 for right triangle calculations."
    )

    function_choice = get_choice_input("Enter your choice (1–1): ", 1, 1)
    #function_choice = get_choice_input("Enter your choice: ")
    while not (1 <= function_choice <= 1):
        get_choice_input("Invalid input. Enter your choice: ")
        function_choice = int(input())

    # Right triangle menu choices
    if function_choice == 1:
        print("Press 1 for Pythagorean Theorem operations.\n"
              "Press 2 to determine if measures form a right triangle.\n"
              "Press 3 to find trigonometric ratios (sin, cos, tan).\n"
              "Press 4 to find acute angle measures of right triangle with sin,cos, and tan.\n"
              "Press 5 to find missing side measure with sin, cos, or tan"
              )
        sub_choice = get_choice_input("Enter your choice (1–5): ", 1, 5)

        # Pythagorean theorem menu
        if sub_choice == 1:
            letter_choice = get_letter_choice("Enter which side you want to solve for: a, b, or c: ")
            while letter_choice not in ["a", "b", "c"]:
                print("Invalid letter choice.")
                letter_choice = get_letter_choice("Enter which side you want to solve for: a, b, or c: ")

            # Solve for legs a or b.
            if letter_choice in ["a", "b"]:
                known_leg = smart_decimal_input("Enter the known leg measure (a or b): ")
                hypotenuse = smart_decimal_input("Enter the measure for the hypotenuse (c): ")
                missing_leg = trig.solve_leg(known_leg, hypotenuse)
                
                print(f"The measure of the missing leg a is {missing_leg}")

            # Solve for the hypotenuse
            elif letter_choice == "c":
                leg_1 = smart_decimal_input("Enter the measure for side a: ")
                leg_2 = smart_decimal_input("Enter the measure for side b: ")
                hypotenuse = trig.solve_hypotenuse(leg_1, leg_2)
                print(f"The measure of the hypotenuse is {hypotenuse}.")
        
        # Determine if measures form a right triangle.
        elif sub_choice == 2:
            side_1 = smart_decimal_input("Enter side 1 length: ")
            side_2 = smart_decimal_input("Enter side 2 length: ")
            side_3 = smart_decimal_input("Enter side 3 length: ")
            sides = sorted([side_1, side_2, side_3])

            if (sides[0]**2 + sides[1]**2) == sides[2]**2:
                print("These are the measurements of a right right triangle.")
            else:
                print("These are not the measurements of a right triangle.")
                
        # Find trigonometric ratios
        elif sub_choice == 3:
            sub_trig_ratio_choice = get_choice_input("Press 1 to find sin ratio.\n"
                  "Press 2 to find cos ratio.\n"
                  "Press 3 to find tan ratio.", 1, 3)
            # Find sin ratio.
            if sub_trig_ratio_choice == 1:
                opposite_leg = smart_decimal_input("Enter the measure of the opposite leg.")
                hypotenuse = smart_decimal_input("Enter the measure of the hypotenuse.")
                sin_ratio = trig.find_sin_ratio(opposite_leg, hypotenuse)
                print(f"The sin ratio is {sin_ratio}.")
            # Find cos ratio.
            elif sub_trig_ratio_choice == 2:
                adjacent_leg = smart_decimal_input("Enter the measure of the adjacent leg.")
                hypotenuse = smart_decimal_input("Enter the measure of the hypotenuse.")
                cos_ratio = trig.find_cos_ratio(adjacent_leg, hypotenuse)
                print(f"The cos ratio is {cos_ratio}.")
            # Find tan ratio.
            elif sub_trig_ratio_choice == 3:
                opposite_leg = smart_decimal_input("Enter the measure of the opposite leg.")
                adjacent_leg = smart_decimal_input("Enter the measure of the adjacent leg.")
                tan_ratio = trig.find_tan_ratio(opposite_leg, adjacent_leg)
                print(f"The tan ratio is {tan_ratio}.")

        # Find acute angle measure using sin, cos, and tan.
        elif sub_choice == 4:
            find_acute_angle_choice = get_choice_input(
            "Press 1 to find angle measure to nearest degree using sin.\n"
            "Press 2 to find angle measure to nearest degree using cos.\n"
            "Press 3 to find angle measure to nearest degree using tan.", 1, 3
            )

            if find_acute_angle_choice == 1:
                while True:
                    sin_ratio = smart_decimal_input("Enter sin ratio: ")
                    if 0 <= sin_ratio <= 1:
                        angle_measure = trig.find_angle_from_sin(sin_ratio)
                        print(f"The angle is approximately {angle_measure}°")
                        break
                    else:
                        print("Invalid sin ratio. Value must be greater than 0 and less than or equal to 1.")

            elif find_acute_angle_choice == 2:
                while True:
                    cos_ratio = smart_decimal_input("Enter cos ratio: ")
                    if 0 <= cos_ratio <= 1:
                        angle_measure = trig.find_angle_from_cos(cos_ratio)
                        print(f"The angle is approximately {angle_measure}°")
                        break
                    else:
                        print("Invalid cos ratio. Value must be greater than 0 and less than or equal to 1.")

            elif find_acute_angle_choice == 3:
                while True:
                    tan_ratio = smart_decimal_input("Enter tan ratio: ")
                    if tan_ratio > 0:
                        angle_measure = trig.find_angle_from_tan(tan_ratio)
                        print(f"The angle is approximately {angle_measure}°")
                        break
                    else:
                        print("Invalid tan ratio. Value must be greater than 0.")

        # Solve right triangle measurements using sin, cos, and tan.
        elif sub_choice == 5:
            trig_identity_choice = get_choice_input(
            "Press 1 to solve with sin.\n"
            "Press 2 to solve with cos.\n"
            "Press 3 to solve with tan.", 1, 3)

            if trig_identity_choice == 1:  # SIN
                angle_measure = smart_decimal_input("Enter known acute angle measure (degrees).")
                while not (0 < angle_measure < 90):
                    print("Invalid angle. Must be between 0° and 90°.")
                    angle_measure = smart_decimal_input("Enter known acute angle measure (degrees).")
                
                leg_choice = get_choice_input(
                    "Press 1 to enter known hypotenuse.\n"
                    "Press 2 to enter known opposite leg.", 1, 2
                )
                
                if leg_choice == 1:
                    hypotenuse = smart_decimal_input("Enter the hypotenuse length.")
                    while hypotenuse <= 0:
                        print("Invalid input. Length must be a positive number.")
                        hypotenuse = smart_decimal_input("Enter the hypotenuse length.")
                    missing_leg_keyword = "opposite leg"
                    opposite_leg = trig.find_missing_side_from_sin(
                        angle_measure, hypotenuse, missing_leg_keyword
                    )
                    print(f"The opposite leg measure is {opposite_leg}.")

                elif leg_choice == 2:
                    opposite_leg = smart_decimal_input("Enter the opposite leg measurement.")
                    while opposite_leg <= 0:
                        print("Invalid input. Length must be a positive number.")
                        opposite_leg = smart_decimal_input("Enter the opposite leg measurement.")
                    missing_leg_keyword = "hypotenuse"
                    hypotenuse = trig.find_missing_side_from_sin(
                        angle_measure, opposite_leg, missing_leg_keyword
                    )
                    print(f"The hypotenuse is {hypotenuse}.")

            elif trig_identity_choice == 2:  # COS
                angle_measure = smart_decimal_input("Enter known acute angle measure (degrees).")
                while not (0 < angle_measure < 90):
                    print("Invalid angle. Must be between 0° and 90°.")
                    angle_measure = smart_decimal_input("Enter known acute angle measure (degrees).")
                
                leg_choice = get_choice_input(
                    "Press 1 to enter known hypotenuse.\n"
                    "Press 2 to enter known adjacent leg.", 1, 2
                )
                
                if leg_choice == 1:
                    hypotenuse = smart_decimal_input("Enter the hypotenuse length.")
                    while hypotenuse <= 0:
                        print("Invalid input. Length must be a positive number.")
                        hypotenuse = smart_decimal_input("Enter the hypotenuse length.")
                    missing_leg_keyword = "adjacent leg"
                    adjacent_leg = trig.find_missing_side_from_cos(
                        angle_measure, hypotenuse, missing_leg_keyword
                    )
                    print(f"The adjacent leg measure is {adjacent_leg}.")

                elif leg_choice == 2:
                    adjacent_leg = smart_decimal_input("Enter the adjacent leg measurement.")
                    while adjacent_leg <= 0:
                        print("Invalid input. Length must be a positive number.")
                        adjacent_leg = smart_decimal_input("Enter the adjacent leg measurement.")
                    missing_leg_keyword = "hypotenuse"
                    hypotenuse = trig.find_missing_side_from_cos(
                        angle_measure, adjacent_leg, missing_leg_keyword
                    )
                    print(f"The hypotenuse is {hypotenuse}.")

            elif trig_identity_choice == 3:
                angle_measure = smart_decimal_input("Enter known acute angle measure (degrees).")
                while not (0 < angle_measure < 90):
                    print("Invalid angle measurement. Angle measure must be greater than 0° and less than 90°.")
                    angle_measure = smart_decimal_input("Enter known acute angle measure (degrees).")

                leg_choice = get_choice_input(
                    "Press 1 to enter known opposite leg measurement.\n"
                    "Press 2 to enter known adjacent leg measurement.", 1, 2
                )
                
                if leg_choice == 1:
                    opposite_leg = smart_decimal_input("Enter the opposite leg measurement.")
                    while opposite_leg <= 0:
                        print("Invalid input. Leg length must be a positive number.")
                        opposite_leg = smart_decimal_input("Enter the opposite leg measurement.")
                    missing_leg_keyword = "adjacent leg"
                    adjacent_leg = trig.find_missing_side_from_tan(
                        angle_measure, opposite_leg, missing_leg_keyword
                    )
                    print(f"The missing adjacent leg measure is {adjacent_leg}.")

                elif leg_choice == 2:
                    adjacent_leg = smart_decimal_input("Enter the adjacent leg measurement.")
                    while adjacent_leg <= 0:
                        print("Invalid input. Leg length must be a positive number.")
                        adjacent_leg = smart_decimal_input("Enter the adjacent leg measurement.")
                    missing_leg_keyword = "opposite leg"
                    opposite_leg = trig.find_missing_side_from_tan(
                        angle_measure, adjacent_leg, missing_leg_keyword
                    )
                    print(f"The missing opposite leg measure is {opposite_leg}.")


                    




if __name__ == "__main__":
    terminate_program = True

    while terminate_program:
        run_trigonometry_menu()

        print("Press 'y' to continue or 'q' to exit")
        user_quit = input().lower()
        while user_quit not in ["y", "q"]:
            print("Invalid response. Press 'y' to continue or 'q' to exit ")
            user_quit = input().lower()

        if user_quit == "q":
            terminate_program = False
