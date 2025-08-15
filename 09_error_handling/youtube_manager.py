import json


# if there exist a file then load that in form oj JSON data other wise return an empty list
def load_data():
    try:
        with open('youtube.txt' , 'r') as file :
            test = json.load(file) # it automatically loads the text in the file and convert that into json data
            print(type(test))
            return test 
    except FileNotFoundError: # if the file is not found
        return [] # return an empty list 


# it will save the video list when the user give the video name and time  it will save that into the youtube.txt file so we use W and dump   
def save_data_helper(videos):
    with open('youtube.txt' , 'w') as file :
        json.dump(videos , file)


# This will list all videos one by one with indexing itself
def list_all_videos(videos) :
    for index ,video in enumerate(videos , start = 1 ) :
        print(f"{index} . {video['name']} , Duration : {video['time']}")
   



def add_video(videos):
    name = input("Enter the name of the video : ")
    time = input("Enter the video time  : ")
    videos.append({'name': name , 'time': time})
    save_data_helper(videos)

def update_video(videos):
  
    vid_num = int(input("which video you want to update : "))
    name = input("which name you want to update : ")
    time = input("which time you want to update : ")
    videos[vid_num - 1]['name'] = name
    videos[vid_num - 1]['time'] = time
    print(videos)
    

def delete_video(videos):
    vid_num = int(input("which video you want to delete : "))
    videos.pop(vid_num - 1)
    print("video cleared successfully")



def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager")
        print("1. List all YT videos")
        print("2. Add a youtube video")
        print("3. Update the YT video details")
        print("4. Delete the YT video")
        print("5. Exit the App")
        choice = input("Enter your choice: ")
        
       

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")
# id the file name is main then execute the main function 
if __name__ == "__main__":
    main() 