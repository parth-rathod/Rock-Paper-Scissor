import random

def logic(k1,k2,user_points,comp_points):
    if k1==k2:
        print("You choose " +k1+" Computer choose " +k2+". Hence DRAW")
        user_points = user_points
        comp_points = comp_points
        return user_points,comp_points
    elif k1 =='R' and k2 =="P":
        print("You choose " +k1+" Computer choose " +k2+". Hence Computer Wins")
        user_points = user_points
        comp_points += 1
        return user_points,comp_points
    elif k1 =='R' and k2 =="S":        
        print("You choose " +k1+" Computer choose " +k2+". Hence You Win")
        user_points += 1
        comp_points = comp_points
        return user_points,comp_points
    elif k1 =='P' and k2 =="R":        
        print("You choose " +k1+" Computer choose " +k2+". Hence You Win")
        user_points += 1
        comp_points = comp_points
        return user_points,comp_points
    elif k1 =='P' and k2 =="S":        
        print("You choose " +k1+" Computer choose " +k2+". Hence Computer Wins")
        user_points = user_points
        comp_points += 1
        return user_points,comp_points
    elif k1 =='S' and k2 =="R":       
        print("You choose " +k1+" Computer choose " +k2+". Hence Computer Wins")
        user_points = user_points
        comp_points += 1
        return user_points,comp_points
    elif k1 =='S' and k2 =="P":        
        print("You choose " +k1+" Computer choose " +k2+". Hence You Win")
        user_points += 1
        comp_points = comp_points
        return user_points,comp_points


if __name__ == "__main__":
    User_name = input("Enter Name:")
    print("\n")
    no_games = int(input (User_name+" how many games you want to play 3 or 5?:"))
    print("\n")
    count = 0
    user_points = 0
    comp_points = 0
    while count < no_games:
        count += 1
        user_input = (input("Choose Rock 'R' or Scissor 'S' or Paper 'P': " )).upper()
        comp_input = random.choices(['R','S','P'])
        user_points,comp_points =logic(user_input,comp_input[0],user_points,comp_points)
        print("User Points:",user_points)
        print("Computer Points:",comp_points)
        print("\n")
