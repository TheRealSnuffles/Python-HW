def main():
    video_file=open("video_times.txt",'r')
    total=0.0
    count=0.0
    for line in video_file:
        run_time=float(line)
        count+=1
        print("Video#", count,":",run_time,sep='')
        total+=run_time
    video_file.close()
    print("The total running time is: ", format(total, '.2f'),'seconds')
main()

