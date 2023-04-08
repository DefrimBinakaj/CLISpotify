import sqlite3
from getpass import getpass
# from minip1db import minip1db.DBPath
import time
import minip1db
# from matplotlib import artist

connection = sqlite3.connect(minip1db.DBPath)
c = connection.cursor()


def login_function():


    global connection, cursor, c, DBPath
    print("CONFIRMED! : ", minip1db.DBPath)

    # connect to the db

    c = connection.cursor()


    # print msg and inputs
    print("---------------- Welcome ----------------")
    userID = input("userID: ")
    password = getpass("password: ")



    # execute to check if both user and artist -------------------------------------
    c.execute(
        '''
        select artists.name from artists, users where artists.aid = :userID and artists.aid = users.uid
        '''
    , {"userID":userID, "password":password})
    if c.fetchall():
        # allow option between user or artist
        userorartist = input("- Do you want to login as a user or an artist: ")
        if userorartist == 'user':
            c.execute(
                '''
                select name from users WHERE uid = :userID and pwd = :password
                '''
            , {"userID":userID, "password":password})
            if c.fetchall():
                user_menu(userID, password)
            else:
                # user_signup(userID, password)
                print("- Incorrect password; returning to log in")
                login_function()
        elif userorartist == 'artist':
            c.execute(
                '''
                select name from artists WHERE aid = :userID and pwd = :password
                '''
            , {"userID":userID, "password":password})
            if c.fetchall():
                artist_menu(userID, password)
            else:
                print("- Incorrect password; returning to log in")
                login_function()
        else:
            # rerun if neither user or artist is selected
            print("- Please input either 'user' or 'artist' ")
            login_function()

    # if not both, check for either -------------------------------------
    else:

        # use a isNeither boolean to ensure that user_signup() is only ran when it is neither
        isNeither = True
        
        # check to see if only user
        c.execute(
            '''
            select name from users WHERE uid = :userID and pwd = :password
            '''
        , {"userID":userID, "password":password})
        if c.fetchall():
            isNeither = False
            user_menu(userID, password)



        # check to see if only artist
        c.execute(
            '''
            select name from artists WHERE aid = :userID and pwd = :password
            '''
        , {"userID":userID, "password":password})
        if c.fetchall():
            isNeither = False
            artist_menu(userID, password)
        

        # run user_signup() if it is neither
        if isNeither == True:
            user_signup(userID, password)


    connection.commit()
    # c.close()










def user_signup(userID, password):

    global connection, cursor, c, DBPath
    c = connection.cursor()


    print("- You do not have an account, you must sign up:")
    uniqueUID = input("unique UID: ")
    username = input("username: ")
    userpwd = getpass("password: ")

    userID = uniqueUID
    password = userpwd



    # ensure that inputted uid is unique
    executeSignup = True

    c.execute(
            '''
            select uid from users WHERE uid = :userID
            '''
        , {"userID":userID})
    if c.fetchall():
        print("- Error: uid not unique; please try again")
        executeSignup = False
        user_signup(userID, password)


    if executeSignup == True:

        c.execute(
            '''
            insert into users (uid, name, pwd) VALUES (:uniqueUID, :username, :password);
            '''
        , {"uniqueUID":userID, "username":username, "password":password})


        c.execute('''
        select uid, name, pwd from users where uid = :uniqueUID
        ''', {"uniqueUID":userID})


        connection.commit()
        print("")
        # used for testing insert:
        # print("user info: ", c.fetchall())

        user_menu(userID, password)





# menu -----------------------------------------------------------------------------------------

def user_menu(userID, password):

    while True:
        userMenuInput = 0
        print("- User Menu:")
        print("1. Start a session")
        print("2. Search for songs / playlists")
        print("3. Search for artists")
        print("4. End the session")
        print("5. Log out")
        print("6. Exit directly")
        userMenuInput = int(input("- Enter number: "))

        if userMenuInput == 1:
            start_session(userID, password)
            userMenuInput = 0
        elif userMenuInput == 2:
            searchSong(userID, password)
            userMenuInput = 0
        elif userMenuInput == 3:
            searchArtist(userID, password)
            userMenuInput = 0
        elif userMenuInput == 4:
            end_session(userID, password)
            userMenuInput = 0
        elif userMenuInput == 5:
            end_session(userID, password)
            login_function()
            break
        elif userMenuInput == 6:
            break
        else:
            print("- Please enter a proper selection")




def artist_menu(userID, password):

    while True:
        print("- Artist Menu:")
        print("1. Add a song")
        print("2. Find top fans and playlists")
        print("3. Log out")
        print("4. Exit directly")
        userMenuInput = int(input("- Enter number: "))
        if userMenuInput == 1:
            artist_add_song()
        elif userMenuInput == 2:
            artist_find_top(userID)
        elif userMenuInput == 3:
            login_function()
            break
        elif userMenuInput == 4:
            break
        else:
            print("- Please enter a proper selection")









def start_session(userID, password):
    # Find all session numbers where uid = login.uid

    global connection, cursor, c, DBPath
    c = connection.cursor()

    

    c.execute(
        '''
        select sessions.end
        from sessions 
        where sessions.uid = :userID
        and sessions.end IS NULL
        order by sno DESC LIMIT 1
        '''
    ,{"userID":userID})


    allNulls = c.fetchall()


    if not allNulls:
        print("Creates a session for the User ID:", userID)
        c.execute("SELECT sno FROM sessions WHERE uid =:userID", {"userID":userID})
        row = c.fetchall()
        
        maxNo = 0
        for entry in row:
            if (entry[0] > maxNo):
                maxNo = entry[0]
        #print(maxNo)
        currentSno = maxNo + 1
        currentDate = time.strftime("%Y-%m-%d %H:%M:%S")
        data = (userID, currentSno, currentDate)
        
        c.execute("INSERT INTO sessions values (?, ?, ?, NULL);", data)
        connection.commit()

    else:
        print("You already have a current session")


    connection.commit()











def end_session(userID, password):

    global connection, cursor, c, DBPath
    c = connection.cursor()




    c.execute(
        '''
        select sessions.end
        from sessions 
        where sessions.uid = :userID
        and sessions.end IS NULL
        order by sno DESC LIMIT 1
        '''
    ,{"userID":userID})


    allNotNulls = c.fetchall()

    if allNotNulls:

        print("Ends a session for the User ID:", userID)
        c.execute("SELECT sno FROM sessions WHERE uid =:userID", {"userID":userID})
        row = c.fetchall()
        currentNo = 0
        
        for entry in row:
            if (entry[0] > currentNo):
                currentNo = entry[0]
        
        endDate = time.strftime("%Y-%m-%d %H:%M:%S")
        
        c.execute("UPDATE sessions SET end=? WHERE uid =? AND sno =?;", (endDate, userID, currentNo))
        connection.commit()
    else:
        print("You have not created a session")
    
    connection.commit()
    
    










# artist functions

def artist_add_song():

    global connection, cursor, c, DBPath
    c = connection.cursor()

    # find the unique sid to be added
    c.execute(
    '''
    select max(sid) from songs
    ''' )
    songEntries = c.fetchall()
    uniqueSID = 0
    for songN in songEntries:        
        uniqueSID = int(songN[0]) + 1
        break

    

    # take title and duration input
    songTitle = input("- Song title: ")
    songDuration = input("- Song duration: ")

    # get sids
    c.execute(
        '''
        select sid from songs WHERE title = :songTitle and duration = :songDuration
        '''
    , {"songDuration":songDuration, "songTitle":songTitle})


    # differentiate between same and not same
    isSameTitle = False

    if c.fetchall():
        isSameTitle = True





    # insert the song if not same
    if isSameTitle == False:

        # artists input
        print("- Enter all artists who performed the song: ")
        allArtists = list(input().split())

        for i in range(len(allArtists)):
            c.execute(
            '''
            insert into perform (aid, sid) VALUES (:artistN, :uniqueSID);
            '''
            , {"artistN":allArtists[i], "uniqueSID":uniqueSID})



        c.execute(
        '''
        insert into songs (sid, title, duration) VALUES (:uniqueSID, :songTitle, :songDuration);
        '''
        , {"uniqueSID":uniqueSID, "songTitle":songTitle, "songDuration":songDuration})
    
    
    
    else:
        print("- Error; there is another song with the same title and duration")

    connection.commit()







def artist_find_top(userID):

    global connection, cursor, c, DBPath
    c = connection.cursor()

    
    # print top 3 users
    c.execute(
    '''
    select users.uid from listen, users, artists, perform
    where artists.aid = :userID
    and artists.aid = perform.aid
    and perform.sid = listen.sid
    and listen.uid = users.uid
    group by users.uid
    order by max(listen.cnt) DESC LIMIT 3
    ''', {"userID":userID})

    print("- Top 3 users who listen to your songs the longest time:")
    top3Users = c.fetchall()
    for topUser in top3Users:
        print(topUser[0])



    # print top 3 playlists
    c.execute(
    '''
    select playlists.title from artists, perform, plinclude, playlists
    where artists.aid = :userID
    and artists.aid = perform.aid
    and perform.sid = plinclude.sid
    and plinclude.pid = playlists.pid
    group by playlists.title
    order by max(plinclude.sid) DESC LIMIT 3
    ''', {"userID":userID})

    print("- Top 3 playlists that include the largest number of your songs:")
    top3Playlists = c.fetchall()
    for topPlaylist in top3Playlists:
        print(topPlaylist[0])


    connection.commit()

















# NEED TO CHECK IF ONE WORD SONG ALREADY EXISTS IN RESULTS, IF NOT EXECUTE QUERY
def searchSong(userID, password):

    global connection, cursor, c, DBPath
    c = connection.cursor()
    
    # Prompts user to search for a song
    songInput = input("Enter a song/playlist to search: ")
    keywords = songInput.split() # Splitting user input into keyword list
    data = [] 
    songQuery = "SELECT sid, title, duration FROM songs WHERE title like ?"
    data.append('% ' + keywords[0])
    
    for each in range(len(keywords)):
        if each == 0:
            songQuery += "OR title like ?"
            songQuery += "OR title like ?"
            data.append('% ' + keywords[each] + ' %')
            data.append(keywords[each] + ' %')
        else:
            songQuery += "OR title like ?"
            songQuery += "OR title like ?"
            songQuery += "OR title like ?"
            data.append('%' + keywords[each])
            data.append('% ' + keywords[each] + ' %')
            data.append(keywords[each] + '%')
            
    songQuery += "ORDER BY ((title like ?)"
    data.append('%' + keywords[0] + '%')
    for each in range(len(keywords)):
        if each == 0:
            songQuery += "+ (title like ?)"
            songQuery += "+ (title like ?)"
            data.append('%' +keywords[each] + '%')
            data.append('%' +keywords[each] + '%')
        else:
            songQuery += "+ (title like ?)"
            songQuery += "+ (title like ?)"
            songQuery += "+ (title like ?)"
            data.append('%' +keywords[each] + '%')
            data.append('%' +keywords[each] + '%')
            data.append('%' +keywords[each] + '%')
    
    songQuery += ");" # Ends the query
        
    c.execute(songQuery, data)
    
    songs = c.fetchall()
    songs.reverse() # Reverse row of songs to get desired result
    
    data = [] 
    playlistQuery = '''SELECT playlists.pid, playlists.title, sum(duration)
    FROM playlists,  songs
    WHERE playlists.title LIKE ?'''
    
    data.append('% ' + keywords[0])

  
    for each in range(len(keywords)):
        if each == 0:
            playlistQuery += "OR playlists.title like ?"
            playlistQuery += "OR playlists.title like ?"
            data.append('% ' + keywords[each] + ' %')
            data.append(keywords[each] + ' %')
        else:
            playlistQuery += "OR playlists.title like ?"
            playlistQuery += "OR playlists.title like ?"
            playlistQuery += "OR playlists.title like ?"
            data.append('%' + keywords[each])
            data.append('% ' + keywords[each] + ' %')
            data.append(keywords[each] + '%')
            
            
    playlistQuery += "GROUP BY playlists.pid, playlists.title "

    playlistQuery += "ORDER BY ((playlists.title like ?)"
    data.append('%' + keywords[0] + '%')
    for each in range(len(keywords)):
        if each == 0:
            playlistQuery += "+ (playlists.title like ?)"
            playlistQuery += "+ (playlists.title like ?)"
            data.append('%' +keywords[each] + '%')
            data.append('%' +keywords[each] + '%')
        else:
            playlistQuery += "+ (playlists.title like ?)"
            playlistQuery += "+ (playlists.title like ?)"
            playlistQuery += "+ (playlists.title like ?)"
            data.append('%' +keywords[each] + '%')
            data.append('%' +keywords[each] + '%')
            data.append('%' +keywords[each] + '%')
    
    
    playlistQuery += ");" # Ends the query
    c.execute(playlistQuery, data)
    playlists = c.fetchall()
    playlists.reverse() # Reverse row of songs to get desired result
    
    
    
    
    
    results = []
    isSongOrArtist = []
    
    for song in songs:
        results += (song[:],)
        isSongOrArtist.append("s")
            
    for playlist in playlists:
        results += (playlist[:],)
        isSongOrArtist.append("p")
    
    for i in range(len(results)):
        if i < len(results)-1:
            print("(", i+1, ":", isSongOrArtist[i],")", end = " ")
        else:
            print("(", i+1, ":", isSongOrArtist[i],")")
            
    

    
    
    
    c.execute("SELECT sid, title, duration FROM songs WHERE title = ?", (songInput, ))
    test = c.fetchall()
    found = False
    i = 0
                
    c.execute('''SELECT playlists.pid, playlists.title, sum(duration)
    FROM playlists, plinclude, songs
    WHERE playlists.pid = plinclude.pid
    AND plinclude.sid = songs.sid
    AND playlists.title = ? ''', (songInput, ))
    test2 = c.fetchall()
    
    
    
    found = False
    i = 0
    for result in test:
        if test[0][1] == results[i][1]:
            found = True
        i += 1
    
    found2 = False
    i = 0
    for result in test2:
        if test2[0][1] == results[i][1]:
            found2 = True
        i += 1
    
    if not found:
        for result in test:
            results.append(result)
    
    if not found2:
        for result in test2:
            results.append(result)
        
    
    selectedSid = print5(results)
    
    
    
    selecting = True
    
    while selecting:
        
        if isSongOrArtist[choice-1] == "s":
            prompt = input('''Song selected, please select one of the options:
            1. Listen to selected song.
            2. See more information about selected song
            3. Add selected song to playlist.
            Enter option #: ''')
            if prompt.isdigit():
                if int(prompt) == 1:
                    listenToSong(selectedSid, userID, password) #  USER ID FIX
                    selecting = False
                elif int(prompt) == 2:
                    seeMoreInformation(selectedSid,isSongOrArtist)
                    selecting = False
                elif int(prompt) == 3:
                    pass
                    addToPlaylist(selectedSid, userID, password)
                    selecting = False
                else:
                    print("Invalid input. Please try again")
        elif isSongOrArtist[choice-1] == "p":
            selectedPid = results[choice-1][0]
            
            c.execute('''
            SELECT songs.sid, songs.title, songs.duration
            FROM songs, playlists, plinclude
            WHERE songs.sid = plinclude.sid
            AND playlists.pid = ?
            AND plinclude.pid = playlists.pid
            ''', (selectedPid, ))
            
            foundSongs = c.fetchall()
            
            results = []
            isSongOrArtist = []
    
            for song in foundSongs:
                results += (song[:],)
                isSongOrArtist.append("s")
            
            selectedSid2 = print5(foundSongs)
            
            prompt = input('''Song selected, please select one of the options:
            1. Listen to selected song.
            2. See more information about selected song
            3. Add selected song to playlist.
            Enter option #: ''')
            if prompt.isdigit():
                if int(prompt) == 1:
                    listenToSong(selectedSid2, userID, password) #  USER ID FIX
                    selecting = False
                elif int(prompt) == 2:
                    seeMoreInformation(selectedSid2,isSongOrArtist)
                    selecting = False
                elif int(prompt) == 3:
                    pass
                    addToPlaylist(selectedSid2)
                    selecting = False
                else:
                    print("Invalid input. Please try again")
         
            selecting = False
            
            
        else:
            print("Invalid input. Please try again")
            
            
        
    connection.commit()

    
    # Return song, id, title & duration
    # Display at most 5 matches at a time, if user clicks
    # select more, displays 5 more matches
    # When a song is displayed a user, a user should be able to select and perform a song


def searchArtist(userID, password):

    global connection, cursor, c, DBPath
    c = connection.cursor()
    
    # Prompts user to search for a song
    artistInput = input("Enter an artist to search: ")
    keywords = artistInput.split() # Splitting user input into keyword list
    
    if len(keywords) == 0:
        print("Error Search, nothing entered...")

    for i in range(len(keywords)):
        c.execute('''
        SELECT DISTINCT artists.aid, artists.name, artists.nationality, count(songs.sid)
        FROM artists, perform, songs
        WHERE artists.aid = perform.aid
        AND songs.sid = perform.sid
        AND artists.name like ?
        GROUP BY artists.aid, artists.name, artists.nationality;
        ''', ("%" + keywords[i] +"%", ))
    artists = c.fetchall()
    artists.reverse()
    

    for i in range(len(keywords)):
        c.execute('''
            SELECT artists.aid, artists.name, artists.nationality
            FROM artists, songs, perform
            WHERE songs.title like ?
            AND songs.sid = perform.sid
            AND perform.aid = artists.aid
            GROUP BY artists.aid, artists.name, artists.nationality
        ''', ("%" + keywords[i] + "%", ))
    
    performs = c.fetchall()
    performs.reverse()
    
    results = []
    
    for artist in artists:
        results += (artist[:], )

    for titles in performs:
        results += (titles[:], )
    

    
    printArtists(results)
    
    selecting = True
    
    # Print all songs for selected artist
    
    c.execute('''SELECT songs.sid, songs.title, songs.duration
    FROM songs, artists, perform
    WHERE songs.sid = perform.sid
    AND perform.aid = artists.aid
    AND artists.aid = ?
    ''', (results[choice-1][0], ))
    
    foundSongs = c.fetchall()
    
    isSong = []
    results = []
    for song in foundSongs:
        results += (song[:],)
        isSong.append("s")
        
    selectedSid = print5(foundSongs)
    
    selecting = True
    
    while selecting:
        if isSong[choice-1] == "s":
            prompt = input('''Song selected, please select one of the options:
            1. Listen to selected song.
            2. See more information about selected song
            3. Add selected song to playlist.
            Enter option #: ''')
            if prompt.isdigit():
                if int(prompt) == 1:
                    listenToSong(selectedSid, userID, password) #  USER ID FIX
                    selecting = False
                elif int(prompt) == 2:
                    seeMoreInformation(selectedSid,isSong)
                    selecting = False
                elif int(prompt) == 3:
                    pass
                    addToPlaylist(selectedSid, userID, password)
                    selecting = False
                else:
                    print("Invalid input. Please try again")
        

  
  
def print5(results):
    global choice
    songs = []
    for result in results:
        songs.append(result)
    
    lastPageResults = len(songs) % 5
    pages = int((len(songs) - lastPageResults) / 5) + 1
    searching = True
    currentPage = 0

    while searching == True:
        if (currentPage < pages-1):
            i = 0
            values = []
            for i in range(5):
                print(str((currentPage*5+i+1)) + ". " + str(songs[(currentPage*5)+i]))
                values.append(currentPage*5+i+1)
            choice = input("Select a option #, or type next, or type prev: ")
            if choice.isdigit():
                choice = int(choice)
                if choice in range(values[0], values[-1]+1):
                    searching = False
                    print("You have selected the song: " + str(songs[choice-1][1]))
                    return (songs[choice-1][0])
                else:
                    print("invalid choice. Please try again.\n===========================================================")
            elif choice == "next" and currentPage < (pages-1):
                currentPage += 1
                print("===========================================================")
            elif choice == "next" and currentPage == (pages-1):
                print("invalid choice. Please try again.\n")
            elif choice == "prev" and currentPage > 0:
                currentPage -=1
                print("===========================================================")
            elif choice == "prev" and currentPage == 0:
                print("invalid choice. PLease try again.\n===========================================================")
        elif (currentPage == pages-1) and lastPageResults == 1:
            i = 0
            values = []
            for i in range(lastPageResults):
                print(str((currentPage*5+i+1)) + ". " + str(songs[(currentPage*5)+i]))
                values.append(currentPage*5+i+1)
            choice = input("Select a option #, or type next, or type prev: ")
            if choice.isdigit():
                choice = int(choice)
                if choice == values[0]:
                    #print((currentPage*5)+(choice-1))
                    searching = False
                    print("You have selected the song: " + str(songs[choice-1][1]))
                    return (songs[choice-1][0])
                else:
                    print("invalid choice. Please try again.\n===========================================================")
            elif choice == "next":
                print("invalid choice. Please try again.\n===========================================================")
            elif choice == "prev":
                currentPage -=1
                print("===========================================================")
        elif (currentPage == pages-1) and lastPageResults != 1:
            i = 0
            values = []
            for i in range(lastPageResults):
                print(str((currentPage*5+i+1)) + ". " + str(songs[(currentPage*5)+i]))
                values.append(currentPage*5+i+1)
            choice = input("Select a option #, or type next, or type prev: ")
            if choice.isdigit():
                choice = int(choice)
                if choice in range(values[0], values[-1]+1):
                    searching = False
                    print("You have selected the song: " + str(songs[choice-1][1]))
                    return songs[choice-1][0]
                else:
                    print("invalid choice. Please try again.\n===========================================================")
            elif choice == "next":
                print("invalid choice. Please try again.\n===========================================================")
            elif choice == "prev" and (pages-1) != 0:
                currentPage -=1
                print("===========================================================")
            elif choice == "prev":
                print("invalid choice. Please try again.\n===========================================================")




def printArtists(artists):
    global choice
    results = artists
    lastPageResults = len(results) % 5
    pages = int((len(results) - lastPageResults) / 5) + 1
    searching = True
    currentPage = 0

    while searching == True:
        if (currentPage < pages-1):
            i = 0
            values = []
            for i in range(5):
                print(str((currentPage*5+i+1)) + ". " + str(results[(currentPage*5)+i]))
                values.append(currentPage*5+i+1)
            choice = input("Select a option #, or type next, or type prev: ")
            if choice.isdigit():
                choice = int(choice)
                if choice in range(values[0], values[-1]+1):
                    searching = False
                    print("You have selected the song: " + str(results[choice-1]))
                    return (results[choice-1])[0]
                else:
                    print("invalid choice. Please try again.\n===========================================================")
            elif choice == "next" and currentPage < (pages-1):
                currentPage += 1
                print("===========================================================")
            elif choice == "next" and currentPage == (pages-1):
                print("invalid choice. Please try again.\n")
            elif choice == "prev" and currentPage > 0:
                currentPage -=1
                print("===========================================================")
            elif choice == "prev" and currentPage == 0:
                print("invalid choice. PLease try again.\n===========================================================")
        elif (currentPage == pages-1) and lastPageResults == 1:
            i = 0
            values = []
            for i in range(lastPageResults):
                print(str((currentPage*5+i+1)) + ". " + str(results[(currentPage*5)+i]))
                values.append(currentPage*5+i+1)
            choice = input("Select a option #, or type next, or type prev: ")
            if choice.isdigit():
                choice = int(choice)
                if choice == values[0]:
                    searching = False
                    print("You have selected the song: " + str(results[choice-1]))
                    return (results[choice-1][0])
                else:
                    print("invalid choice. Please try again.\n===========================================================")
            elif choice == "next":
                print("invalid choice. Please try again.\n===========================================================")
            elif choice == "prev":
                currentPage -=1
                print("===========================================================")
        elif (currentPage == pages-1) and lastPageResults != 1:
            i = 0
            values = []
            for i in range(lastPageResults):
                print(str((currentPage*5+i+1)) + ". " + str(results[(currentPage*5)+i]))
                values.append(currentPage*5+i+1)
            choice = input("Select a option #, or type next, or type prev: ")
            if choice.isdigit():
                choice = int(choice)
                if choice in range(values[0], values[-1]+1):
                    searching = False
                    print("You have selected the song: " + str(results[choice-1]))
                    return results[choice-1][0]
                else:
                    print("invalid choice. Please try again.\n===========================================================")
            elif choice == "next":
                print("invalid choice. Please try again.\n===========================================================")
            elif choice == "prev" and (pages-1) != 0:
                currentPage -=1
                print("===========================================================")
            elif choice == "prev":
                print("invalid choice. Please try again.\n===========================================================")



def listenToSong(selectedSid, userID, password):

    global connection, cursor, c, DBPath
    c = connection.cursor()

    '''
    1.) Listen to a song
    If there is no session for userID, create a session for the user
    If there is a session
    
    If the user has already listened to a song in the table, then increment the cnt in listen table
    If it does not exist in the listen table then insert the row with current sno and other relevant info
    '''
    c.execute("SELECT sno FROM sessions WHERE uid =:userID AND end = NULL", {"userID":userID})
    currentSession = c.fetchall()
    
    if not currentSession:
        #session is empty, create session
        start_session(userID, password)

        c.execute(
        '''
        select sessions.sno
        from sessions 
        where sessions.uid = :userID
        and sessions.end IS NULL
        order by sno DESC LIMIT 1
        '''
        ,{"userID":userID})

        currentSession = c.fetchall()
        print(currentSession)
        connection.commit()


        c.execute("INSERT INTO listen VALUES (?,?,?, 1)", (userID, currentSession[0][0], selectedSid))  
        connection.commit()

    else:       
        # If we have an existing session
        c.execute("SELECT sid, cnt FROM listen WHERE sno = ? AND uid = ?", (currentSession, userID))
        
        songs = c.fetchall()
        found = False
        for song in songs:
            if selectedSid == song[0]:
                found = True
        
        if found:
            c.execute("UPDATE listen SET ? WHERE uid = ? AND sno = ? AND sid = ?", (songs[1]+1, userID, currentSession, selectedSid))
        else:
            c.execute("INSERT INTO listen VALUES (?,?,?,1)", (userID, currentSession, selectedSid))
            
    
    connection.commit()


    '''
    2.) See more information about it
    More information about the selected song would be displaying all artists who have performed the song
    and all the playlists the song appears in
    '''





def seeMoreInformation(selectedSid, isSongOrArtist):

    global connection, cursor, c, DBPath
    c = connection.cursor()


    print(isSongOrArtist)
    global choice

    if isSongOrArtist[int(choice)-1] == 's':
        c.execute("SELECT artists.name FROM perform, artists WHERE perform.sid = ? AND perform.aid = artists.aid", (selectedSid,))
        results = c.fetchall()
        i = 0
        lenResults = len(results)-1
        print("Performed by: ", end="")
        for result in results:
            if i < lenResults:
                print(result[0], end = ", ")
            else:
                print(result[0] + ".")
            i+=1
        
        c.execute('''SELECT playlists.title 
        FROM playlists, plinclude 
        WHERE plinclude.sid = ? 
        AND plinclude.pid = playlists.pid''', (selectedSid, ))
        
        results2 = c.fetchall()
        i = 0
        lenResults2 = len(results2)-1
        print("In playlists: ", end="")
        for result in results2:
            if i < lenResults2:
                print(result[0], end = ", ")
            else:
                print(result[0] + ".")
            i+=1
    elif isSongOrArtist[int(choice)-1] == 'p':
        print("Cannot display more information about a playlist")
        


'''
3.) Add the song to a playlist 
Add a song to the playlist, check if it already exists in the playlist. If not, insert.

Check if playlist exists, if it does, add to that playlist

If playlist does not exist, let us create a new playlist with a unique pid, let user choose a title
with their user id. Will also need to insert into songs into plinclude. sorder max + 1

'''

def addToPlaylist(selectedSid, userID, password):

    global connection, cursor, c, DBPath
    c = connection.cursor()

    
    playlistPrompt = input("Enter playlist name that you would like to add the selected song to: ")
    
    
    c.execute("SELECT title, pid FROM playlists WHERE uid = ?", (userID,))
    
    playlists = c.fetchall()
    
    found = False
   
    for i in range(len(playlists)):
        if playlists[i][0] == playlistPrompt:
            foundPid = playlists[i][1]
            found = True
    
        
    if found == True:
    
        c.execute("SELECT max(sorder) from plinclude where pid = ?", (foundPid, ))
        currentSOrder = c.fetchone()
        
        c.execute("INSERT into plinclude VALUES (?, ?, ?)", (foundPid, selectedSid, currentSOrder[0]+1))
    else:
        # If playlist does not exist, let us create a new playlist with a unique pid, let user choose a title
        # with their user id. Will also need to insert into songs into plinclude. sorder max + 1
        
        c.execute("SELECT max(pid) FROM playlists")
        uniquePid = c.fetchone()[0] + 1
        
        
        c.execute("INSERT INTO playlists VALUES (?,?,?)", (uniquePid, playlistPrompt, userID))
        
        print("Creating playlist: " + playlistPrompt)
    

        c.execute("INSERT into plinclude VALUES (?, ?, ?)", (uniquePid, selectedSid, 1, ))
        print("Inserting selected song into new playlist: " + playlistPrompt)
        
        c.execute("SELECT * FROM plinclude WHERE pid = ?", (uniquePid, ))
    

    results = c.fetchall()
    
    print(results)
    
    connection.commit()

       