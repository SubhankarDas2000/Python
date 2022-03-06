#Write a Python program to display the examination schedule. (extract the date from exam_st_date).
exam_st_date = input("Enter the exam date :")
exam_st_date=exam_st_date.split("/")
print( "The examination will start from : %i / %i / %i"%exam_st_date)
