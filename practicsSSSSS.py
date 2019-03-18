def main():
    num_videos=int(input("Enter the number of videos you have: "))
    video_file=open("video_times.txt", 'w')
    print("Enter the video times: ")
    for count in range(1, num_videos+1):
        run_times=float(input("video #"+str(count)+":"))
        video_file.write(str(run_times)+'\n')
    video_file.close()
    print("The times have been savesd to video_times.txt")
main()


