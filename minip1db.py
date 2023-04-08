

# -*- coding: utf-8 -*-
import sqlite3
import time
import sys

from minip1 import *

DBPath = input("Enter DB name: ")


connection = None
cursor = None

def connectDB(DBPath):
    global connection, cursor
    connection = sqlite3.connect(DBPath)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA forteign_keys=ON; ')
    connection.commit()
    return


def drop_tables():
    global connection, cursor

    drop_perform = "drop table if exists perform;"
    drop_artists = "drop table if exists artists;"
    drop_plinclude = "drop table if exists plinclude;"
    drop_playlist = "drop table if exists playlists;"
    drop_listen = "drop table if exists listen;"
    drop_sessions = "drop table if exists sessions;"
    drop_songs = "drop table if exists songs;"
    drop_users = "drop table if exists users;"


    cursor.execute(drop_perform)
    cursor.execute(drop_artists)
    cursor.execute(drop_plinclude)
    cursor.execute(drop_playlist)
    cursor.execute(drop_listen)
    cursor.execute(drop_sessions)
    cursor.execute(drop_songs)
    cursor.execute(drop_users)
    
def create_tables():
    global cursor, connection
    
    user_query = '''create table users (
  uid		char(4),
  name		text,
  pwd		text,
  primary key (uid)
    );
    '''
    
    songs_query = '''
    create table songs (
    sid		int,
    title		text,
    duration	int,
    primary key (sid)
    ); 
    '''
    
    sessions_query = '''
    create table sessions (
    uid		char(4),
    sno		int,
    start 	date,
    end 		date,
    primary key (uid,sno),
    foreign key (uid) references users
	on delete cascade
    );
    '''
    listen_query = '''
    create table listen (
    uid		char(4),
    sno		int,
    sid		int,
    cnt		real,
    primary key (uid,sno,sid),
    foreign key (uid,sno) references sessions,
    foreign key (sid) references songs
    );
    '''
    
    playlist_query = '''
    create table playlists (
    pid		int,
    title		text,
    uid		char(4),
    primary key (pid),
    foreign key (uid) references users
    );
    '''
    
    plinclude_query = '''
    create table plinclude (
    pid		int,
    sid		int,
    sorder	int,
    primary key (pid,sid),
    foreign key (pid) references playlists,
    foreign key (sid) references songs
    );
    '''
    
    artists_query = '''
    create table artists (
    aid		char(4),
    name		text,
    nationality	text,
    pwd		text,
    primary key (aid)
    );
    '''
    
    perform_query = '''
    create table perform (
    aid		char(4),
    sid		int,
    primary key (aid,sid),
    foreign key (aid) references artists,
    foreign key (sid) references songs
    );
    '''
    
    cursor.execute(user_query)
    cursor.execute(songs_query)
    cursor.execute(sessions_query)
    cursor.execute(listen_query)
    cursor.execute(playlist_query)
    cursor.execute(plinclude_query)
    cursor.execute(artists_query)
    cursor.execute(perform_query)
    connection.commit()
    
def insert_data():
    global connection, cursor
    
    insert_users = '''
insert into users values ('u1', 'Maheen Lynn', 'po395');
insert into users values ('u2', 'Leena Markham', 'Dortsimo');
insert into users values ('u3', 'Branden Escobar', '4?Jkwer34');
insert into users values ('u4', 'Digby Tierney', 'Querty44!');
insert into users values ('u5', 'Harriet Beck', 'Rewt34reg');
insert into users values ('u6', 'Aron Gu', 'Dortsimpson15?');
insert into users values ('u7', 'Jeevan Dillard', 'Li430ig2');
insert into users values ('u8', 'Laaibah Cano', 'abc4697');
insert into users values ('u9', 'Ameila Pike', 'abcde');
insert into users values ('u10','Davood Rafiei', 'FyTek4ji');
insert into users values ('u11', 'Spencer Schimdt', 'I8293!!');
insert into users values ('u12', 'Ryder Catonio', '5432rfdsf');
insert into users values ('u13', 'Dradelli Guy', 'wviegio');
insert into users values ('u14', 'Aron Gu', 'L753fweE');
insert into users values ('u15', 'Mark Sanchez', '435operigki4');
insert into users values ('u16', 'Marion Trap', 'poerkfFte56Y6');
insert into users values ('u17', 'Mackenzie Parks', 'peorit45');
insert into users values ('u18', 'Daria Blackburn', 'ofrepki3?');
insert into users values ('u19', 'Samuel Dixon', '3t4otif4i');
insert into users values ('u20','Hamed Mirzaei', 'femferiof2');
insert into users values ('u21', 'Amelia Pike', 'p593i4304kdj');
insert into users values ('u22', 'Quinn Mccartney', '4fo4lfs2309');
insert into users values ('u23', 'Brenden Akhtar', 'o348f4i8');
insert into users values ('u24', 'Catrina Maxwell', '43r3rfkd1');
insert into users values ('u25', 'Darsh Snyder', 'kgf4f499430');
insert into users values ('u26', 'Pheobe Shannon', '3fg349f3');
insert into users values ('u27', 'Judy Walsh', 'efgk304952');
insert into users values ('u28', 'Bret Bartlett', '40fk3i0fk');
insert into users values ('u29', 'Diogo Lowry', '34rf391kes');
insert into users values ('u30', 'Rudra Duke', 'o4kg4pk2');
insert into users values ('u31', 'Mike Smith', '9tf394f31');
insert into users values ('u32', 'Conner Wang', '3fk30tii34');
insert into users values ('u33', 'Saim Hays', '49fr2kasi');
insert into users values ('u34', 'Jeanne Carlson', '340fk3wif');
insert into users values ('u35', 'John-Paul Whittaker', 'i43fk3fri');
insert into users values ('u36', 'Bjorn Partridge', 'apkzmiowrfm');
insert into users values ('u37', 'Dominic Chen', 'ef3f3kpk');
insert into users values ('u38', 'Aleah Mendoza', 'ef3m4r095');
insert into users values ('u39', 'Kiyan Underwood', '34rkr93gfrk');
insert into users values ('u40', 'Wendy Fernandez', '3f3mf2i4');
insert into users values ('u41', 'Shamima Gonzales', 'por3p409');
insert into users values ('u42', 'Mike Smith', '232ed2drfr');
insert into users values ('a41', 'Fake Kendrick Lamar', 'gote');
insert into users values ('a44', 'Christina Aguilera', '3tfj3');
insert into users values ('a56', 'Justin Babe', '3opt54i');
    '''
    
    insert_songs = '''
insert into songs values (1, 'Waka Waka(This Time For Africa)', 202);
insert into songs values (2, 'Applause', 212);
insert into songs values (3, 'Demons', 177);
insert into songs values (4, 'Counting Stars', 259);
insert into songs values (5, 'Wavin flag', 220);
insert into songs values (6, 'Just Give Me a Reason', 242);
insert into songs values (7, 'Stronger(What Doesn`t Kill You)', 222);
insert into songs values (8, 'We Are Young', 233);
insert into songs values (9, 'Moves Like Jagger', 201);
insert into songs values (10, 'Nice for what', 210);
insert into songs values (11, 'Hold on, we are going home', 227);
insert into songs values (12, 'DJ Got Us Fallin` in Love', 221);
insert into songs values (13, 'Wild Ones', 233);
insert into songs values (14, 'Everybody Talks', 179);
insert into songs values (15, 'Good Time', 206);
insert into songs values (16, 'Blame', 214);
insert into songs values (17, 'I Need Your Love', 234);
insert into songs values (18, 'Wake Me Up', 249);
insert into songs values (19, 'Poker Face', 238);
insert into songs values (20, 'Cheap Thrills', 224);
insert into songs values (21, 'No Lie', 221);
insert into songs values (22, 'Gentleman', 194);
insert into songs values (23, 'Titanium', 245);
insert into songs values (24, 'Cool Kids', 237);
insert into songs values (25, 'Chasing The Sun', 199);
insert into songs values (26, 'We Found Love', 215);
insert into songs values (27, 'Give Me Everything', 252);
insert into songs values (28, 'Come & Get It', 231);
insert into songs values (29, 'Me and My Broken Heart', 193);
insert into songs values (30, 'Best Day of My Life', 194);
insert into songs values (31, 'International Love', 227);
insert into songs values (32, 'You Make Me Feel...', 216);
insert into songs values (33, 'Safe and Sound', 193);
insert into songs values (34, 'Burn', 231);
insert into songs values (35, 'Shut Up and Dance', 197);
insert into songs values (36, 'Want to Want Me', 207);
insert into songs values (37, 'Dynamite', 202);
insert into songs values (38, 'Feel This Moment', 229);
insert into songs values (39, 'Hall of Fame', 202);
insert into songs values (40, 'On the Floor', 231);
insert into songs values (41, 'I Feel It Coming', 269);
insert into songs values (42, 'Blinding Lights', 201);
insert into songs values (43, 'My Heart Will Go On', 280);
insert into songs values (44, 'I`m Alive', 210);
insert into songs values (45, 'Complicated', 244);
insert into songs values (46, 'Club Can`t Handle Me', 232);
insert into songs values (47, 'Wannabe', 172);
insert into songs values (48, 'Shape of You', 233);
insert into songs values (49, 'Bad Company', 290);
insert into songs values (50, 'Bad Blood', 211);
insert into songs values (51, 'Peaches', 198);
    '''
    
    insert_sessions = '''
    -- u1 Sessions
insert into sessions values ('u1', 3, '2022-09-23 11:22:33', '2022-09-27 15:32:21');
insert into sessions values ('u1', 2, '2022-02-23 21:17:32', '2022-02-26 22:19:13');
insert into sessions values ('u1', 1, '2021-09-23 12:15:02', '2021-09-24 20:58:57');

-- u2 Sessions
insert into sessions values ('u2', 1, '2021-10-30 08:26:55', '2021-11-03 05:22:44');

-- u3 Sessions
insert into sessions values ('u3', 2, '2022-09-24 04:55:22', '2022-09-25 09:34:48');
insert into sessions values ('u3', 1, '2022-08-25 11:06:10', '2022-08-28 04:02:48');

-- u4 Sessions
insert into sessions values ('u4', 1, '2021-11-17 14:57:16', '2021-11-19 09:03:32');

-- u5 Sessions
insert into sessions values ('u5', 2, '2022-02-17 00:39:33', '2022-02-20 02:52:45');
insert into sessions values ('u5', 1, '2021-01-01 02:30:14', '2021-01-06 01:08:09');

-- u6 Sessions
insert into sessions values ('u6', 2, '2022-01-25 12:47:26', '2022-01-28 01:21:59');
insert into sessions values ('u6', 1, '2021-03-30 13:54:51', '2021-04-01 06:10:09');

-- u7 Sessions
insert into sessions values ('u7', 3, '2022-08-20 14:00:12', '2022-08-23 13:08:39');
insert into sessions values ('u7', 2, '2021-04-25 08:38:57', '2021-04-26 05:37:06');
insert into sessions values ('u7', 1, '2021-01-26 18:50:08', '2021-01-29 08:55:05');

-- u8 Sessions
insert into sessions values ('u8', 2, '2022-04-02 01:12:19', '2022-04-05 15:35:11');
insert into sessions values ('u8', 1, '2022-03-25 20:22:07', '2022-03-28 07:57:12');

-- u9 Sessions
insert into sessions values ('u9', 3, '2022-06-18 10:47:54', '2022-06-22 05:41:23');
insert into sessions values ('u9', 2, '2022-02-08 11:44:32', '2022-02-11 06:02:40');
insert into sessions values ('u9', 1, '2022-01-22 04:40:16', '2022-01-25 15:14:17');

-- u10 Sessions
insert into sessions values ('u10', 3, '2022-09-27 16:28:03', '2022-09-28 13:11:57');
insert into sessions values ('u10', 2, '2022-09-13 07:47:34', '2022-09-16 00:59:59');
insert into sessions values ('u10', 1, '2022-01-28 03:45:23', '2022-01-31 20:01:36');

-- u11 Sessions
insert into sessions values ('u11', 3, '2022-02-02 01:58:33', '2022-02-05 04:58:30');
insert into sessions values ('u11', 2, '2021-11-18 05:12:23', '2021-11-22 12:13:07');
insert into sessions values ('u11', 1, '2021-10-27 02:18:53', '2021-10-30 15:24:27');

-- u12 Sessions
insert into sessions values ('u12', 2, '2021-08-31 06:20:32', '2021-09-02 11:25:08');
insert into sessions values ('u12', 1, '2021-02-19 05:46:30', '2021-02-25 06:08:37');

-- u13 Sessions
insert into sessions values ('u13', 2, '2022-01-19 14:36:54', '2022-01-21 17:42:44');
insert into sessions values ('u13', 1, '2021-06-24 20:23:14', '2021-06-28 00:23:34');

-- u14 Sessions
insert into sessions values ('u14', 2, '2022-03-07 21:22:49', '2022-03-11 08:04:02');
insert into sessions values ('u14', 1, '2021-04-19 22:00:25', '2021-04-23 07:24:14');

-- u15 Sessions
insert into sessions values ('u15', 1, '2022-09-06 00:59:13', '2022-09-09 18:51:12');

-- u16 Sessions
insert into sessions values ('u16', 2, '2022-06-16 17:30:13', '2020-06-18 21:40:57');
insert into sessions values ('u16', 1, '2021-04-15 19:33:20', '2021-04-17 10:19:00');

-- u17 Sessions
insert into sessions values ('u17', 3, '2022-09-02 16:15:53', '2022-09-04 14:17:38');
insert into sessions values ('u17', 2, '2021-12-20 19:00:05', '2021-12-25 14:45:47');
insert into sessions values ('u17', 1, '2021-03-27 19:09:55', '2021-03-28 04:58:00'); 

-- u18 Sessions
insert into sessions values ('u18', 3, '2021-09-23 15:53:44', '2021-09-25 07:16:55');
insert into sessions values ('u18', 2, '2021-05-30 06:13:01', '2021-06-01 16:59:23');
insert into sessions values ('u18', 1, '2021-05-23 06:53:35', '2021-05-26 06:34:09');

-- u19 Sessions
insert into sessions values ('u19', 3, '2022-04-15 09:19:14', '2022-04-18 15:46:10');
insert into sessions values ('u19', 2, '2021-12-31 13:18:02', '2022-01-02 19:21:51');
insert into sessions values ('u19', 1, '2021-05-18 21:12:02', '2021-05-21 07:51:05');

-- u20 Sessions
insert into sessions values ('u20', 1, '2022-09-25 19:43:23', '2022-09-27 01:23:34');

-- u21 Sessions
insert into sessions values ('u21', 1, '2021-08-15 16:27:02', '2021-08-18 07:18:06');

-- u22 Sessions
insert into sessions values ('u22', 2, '2022-09-12 23:58:09', '2022-09-14 02:26:32');
insert into sessions values ('u22', 1, '2021-03-21 04:05:55', '2021-03-24 18:37:27');

-- u23 Sessions
insert into sessions values ('u23', 4, '2022-09-22 20:33:54', '2022-09-23 03:01:08');
insert into sessions values ('u23', 3, '2022-09-08 09:33:46', '2022-09-15 21:11:13');
insert into sessions values ('u23', 2, '2022-06-10 11:00:27', '2022-06-13 12:42:59');
insert into sessions values ('u23', 1, '2022-05-10 03:59:44', '2022-05-14 21:42:02');

-- u24 Sessions
insert into sessions values ('u24', 2, '2021-09-10 16:11:45', '2021-09-14 08:22:57');
insert into sessions values ('u24', 1, '2021-03-24 03:45:32', '2021-03-26 23:47:17');

-- u25 Sessions
insert into sessions values ('u25', 2, '2021-09-15 07:15:04', '2021-09-19 12:38:48');
insert into sessions values ('u25', 1, '2021-01-23 05:09:11', '2021-01-25 04:03:27');

-- u26 Sessions
insert into sessions values ('u26', 2, '2022-05-23 19:08:07', '2022-05-25 13:32:56');
insert into sessions values ('u26', 1, '2021-08-25 20:07:17', '2021-08-28 01:09:57');

-- u27 Sessions
insert into sessions values ('u27', 1, '2021-12-16 12:13:22', '2021-12-20 14:21:46');

-- u28 Sessions
insert into sessions values ('u28', 30, '2022-07-01 16:08:41', '2022-07-05 07:07:14');

-- u29 Sessions
insert into sessions values ('u29', 2, '2022-05-27 00:40:44', '2022-05-31 19:13:18');
insert into sessions values ('u29', 1, '2021-02-28 11:23:21', '2021-03-02 00:24:51');

-- u30 Sessions
insert into sessions values ('u30', 1, '2021-09-26 06:33:27', '2021-09-29 10:21:23');

-- u31 Sessions
insert into sessions values ('u31', 1, '2021-07-12 13:14:14', '2021-07-13 04:36:13');

-- u32 Sessions
insert into sessions values ('u32', 4, '2022-09-22 13:45:51', '2022-09-24 17:54:20');
insert into sessions values ('u32', 3, '2022-09-12 09:55:40', '2022-09-21 22:22:22');
insert into sessions values ('u32', 2, '2022-07-19 23:24:19', '2022-07-23 07:48:39');
insert into sessions values ('u32', 1, '2021-01-23 17:51:27', '2021-01-25 16:17:40');

-- u33 Sessions
insert into sessions values ('u33', 1, '2022-04-28 13:22:19', '2022-04-30 03:45:01');

-- u34 Sessions
insert into sessions values ('u34', 1, '2021-07-15 06:37:33', '2021-07-20 01:20:32');

-- u35 Sessions
insert into sessions values ('u35', 1, '2022-05-20 13:09:07', '2022-05-23 18:39:20');

-- u36 Sessions
insert into sessions values ('u36', 1, '2022-09-24 10:11:22', '2022-09-25 23:23:41');

-- u37 Sessions
insert into sessions values ('u37', 2, '2021-09-30 21:25:51', '2021-10-02 15:26:35');
insert into sessions values ('u37', 1, '2021-02-25 15:04:09', '2021-02-26 13:39:36');

-- u38 Sessions
insert into sessions values ('u38', 2, '2021-10-24 10:35:31', '2021-10-27 19:11:40');
insert into sessions values ('u38', 1, '2021-02-15 20:16:18', '2021-02-18 22:31:58');

-- u39 Sessions
insert into sessions values ('u39', 2, '2022-09-16 08:44:43', '2022-09-18 05:41:21');
insert into sessions values ('u39', 1, '2021-09-06 23:56:55', '2021-09-10 09:13:00');

-- u40 Sessions
insert into sessions values ('u40', 1, '2021-08-23 21:05:04', '2021-08-25 23:58:07');

-- u41 Sessions
insert into sessions values ('u41', 2, '2022-08-22 05:55:17', '2022-08-26 09:15:45');
insert into sessions values ('u41', 1, '2021-04-28 18:13:22', '2021-04-30 20:12:41');

-- u42 Sessions
insert into sessions values ('u42', 3, '2021-11-16 04:51:52', '2021-11-18 17:29:55');
insert into sessions values ('u42', 2, '2021-07-29 22:00:21', '2021-07-31 14:27:04');
insert into sessions values ('u42', 1, '2021-01-15 18:20:14', '2021-01-18 13:27:51');
    '''
    
    insert_listen = '''
    -- u1 Sessions 
insert into listen values ('u1', 3, 2, 3);
insert into listen values ('u1', 3, 12, 5);
insert into listen values ('u1', 3, 16, 4);
insert into listen values ('u1', 2, 20, 20);
insert into listen values ('u1', 2, 21, 23);
insert into listen values ('u1', 2, 6, 18);
insert into listen values ('u1', 1, 44, 63.9);
insert into listen values ('u1', 1, 17, 33.8);
insert into listen values ('u1', 1, 23, 26.5);
insert into listen values ('u1', 1, 29, 39.5);

-- u2 Sessions
insert into listen values ('u2', 1, 1, 5);
insert into listen values ('u2', 1, 8, 8.4);
insert into listen values ('u2', 1, 12, 3.3);
insert into listen values ('u2', 1, 17, 125.4);
insert into listen values ('u2', 1, 2, 63.8);
insert into listen values ('u2', 1, 7, 34.2);
insert into listen values ('u2', 1, 36, 12.7);
insert into listen values ('u2', 1, 37, 19.5);
insert into listen values ('u2', 1, 35, 10.7);

-- u3 Sessions
insert into listen values ('u3', 2, 42, 9.7);
insert into listen values ('u3', 2, 30, 11.8);
insert into listen values ('u3', 2, 14, 23.4);
insert into listen values ('u3', 2, 10, 33.2);
insert into listen values ('u3', 1, 16, 0.5);
insert into listen values ('u3', 1, 30, 14.7);
insert into listen values ('u3', 1, 38, 6.7);
insert into listen values ('u3', 1, 23, 14.4);
insert into listen values ('u3', 1, 42, 15.6);

-- u4 Sessions
insert into listen values ('u4', 1, 29, 10);
insert into listen values ('u4', 1, 11, 20);
insert into listen values ('u4', 1, 51, 9);

-- u5 Sessions
insert into listen values ('u5', 1, 3, 10);
insert into listen values ('u5', 1, 4, 111);
insert into listen values ('u5', 1, 38, 12.23);
insert into listen values ('u5', 1, 6, 23.35);

-- u6 Sessions
insert into listen values ('u6', 2, 43, 10);
insert into listen values ('u6', 2, 4, 6);
insert into listen values ('u6', 2, 5, 11);
insert into listen values ('u6', 2, 40, 22);
insert into listen values ('u6', 1, 32, 12.5);
insert into listen values ('u6', 1, 11, 11.29);

-- u7 Sessions
insert into listen values ('u7', 3, 38, 4.4);
insert into listen values ('u7', 3, 23, 14.2);
insert into listen values ('u7', 3, 27, 39);
insert into listen values ('u7', 3, 42, 22);
insert into listen values ('u7', 2, 15, 32.2);
insert into listen values ('u7', 2, 37, 28.44);
insert into listen values ('u7', 2, 4, 251);
insert into listen values ('u7', 1, 4, 251);

-- u8 Sessions
insert into listen values ('u8', 2, 20, 12.2);
insert into listen values ('u8', 2, 3, 62.3);
insert into listen values ('u8', 2, 31, 2.3);
insert into listen values ('u8', 2, 38, 5.5);
insert into listen values ('u8', 2, 40, 4.5);
insert into listen values ('u8', 2, 26, 12);
insert into listen values ('u8', 2, 24, 8.8);
insert into listen values ('u8', 2, 39, 10);
insert into listen values ('u8', 1, 24, 3.3);
insert into listen values ('u8', 1, 38, 12.5);

-- u9 Sessions
insert into listen values ('u9', 3, 43, 44.3);
insert into listen values ('u9', 3, 26, 25);
insert into listen values ('u9', 3, 16, 29);
insert into listen values ('u9', 3, 36, 25);
insert into listen values ('u9', 3, 21, 20);
insert into listen values ('u9', 3, 37, 22);
insert into listen values ('u9', 3, 41, 22);
insert into listen values ('u9', 1, 40, 12);
insert into listen values ('u9', 1, 5, 6);
insert into listen values ('u9', 1, 43, 5);

-- u10 Sessions
insert into listen values ('u10', 3, 5, 1.2);
insert into listen values ('u10', 3, 11, 2.0);
insert into listen values ('u10', 3, 40, 33);
insert into listen values ('u10', 3, 25, 14);
insert into listen values ('u10', 3, 13, 22);
insert into listen values ('u10', 3, 35, 21);
insert into listen values ('u10', 2, 13, 22);
insert into listen values ('u10', 2, 25, 10);
insert into listen values ('u10', 2, 42, 23.3);
insert into listen values ('u10', 2, 33, 32.5);
insert into listen values ('u10', 1, 25, 9);
insert into listen values ('u10', 1, 13, 0.9);
insert into listen values ('u10', 1, 40, 12);

-- u11 Sessions
insert into listen values ('u11', 2, 11, 21.5);
insert into listen values ('u11', 2, 29, 44);
insert into listen values ('u11', 1, 2, 13.4);
insert into listen values ('u11', 1, 43, 102.2);
insert into listen values ('u11', 1, 9, 9);
insert into listen values ('u11', 1, 8, 14.5);
insert into listen values ('u11', 1, 22, 22);

-- u12 Sessions
insert into listen values ('u12', 2, 41, 32);
insert into listen values ('u12', 2, 23, 5);
insert into listen values ('u12', 2, 10, 29);
insert into listen values ('u12', 2, 16, 5);
insert into listen values ('u12', 1, 25, 32.55);
insert into listen values ('u12', 1, 40, 281);

-- u13 Sessions
insert into listen values ('u13', 2, 40, 4);
insert into listen values ('u13', 2, 5, 5);
insert into listen values ('u13', 1, 14, 5.6);
insert into listen values ('u13', 1, 4, 6.7);
insert into listen values ('u13', 1, 6, 5);
insert into listen values ('u13', 1, 27, 30);
insert into listen values ('u13', 1, 47, 16);

-- u14 Sessions
insert into listen values ('u14', 2, 32, 5.5);
insert into listen values ('u14', 2, 35, 5.5);
insert into listen values ('u14', 2, 29, 5.5);
insert into listen values ('u14', 2, 16, 5.5);
insert into listen values ('u14', 2, 17, 3.1);
insert into listen values ('u14', 2, 34, 2.4);
insert into listen values ('u14', 2, 23, 5.5);
insert into listen values ('u14', 1, 15, 98.34);
insert into listen values ('u14', 1, 37, 46.65);
insert into listen values ('u14', 1, 51, 32);

-- u15 Sessions
insert into listen values ('u15', 1, 42, 29.9);
insert into listen values ('u15', 1, 32, 10.3);
insert into listen values ('u15', 1, 22, 15);
insert into listen values ('u15', 1, 49, 51);

-- u16 Sessions
insert into listen values ('u16', 2, 41, 33);
insert into listen values ('u16', 2, 36, 12);
insert into listen values ('u16', 2, 21, 21);
insert into listen values ('u16', 2, 37, 23);
insert into listen values ('u16', 2, 51, 16);
insert into listen values ('u16', 1, 26, 37.32);
insert into listen values ('u16', 1, 37, 15.89);
insert into listen values ('u16', 1, 15, 18.99);
insert into listen values ('u16', 1, 47, 16);
insert into listen values ('u16', 1, 51, 15.9);

-- u17 Sessions
insert into listen values ('u17', 3, 30, 10.3);
insert into listen values ('u17', 3, 50, 13.3);
insert into listen values ('u17', 2, 18, 5);
insert into listen values ('u17', 2, 34, 6);
insert into listen values ('u17', 2, 17, 4);
insert into listen values ('u17', 2, 20, 6);
insert into listen values ('u17', 2, 21, 8);
insert into listen values ('u17', 2, 16, 5.4);
insert into listen values ('u17', 1, 15, 11.83);
insert into listen values ('u17', 1, 32, 101.22);
insert into listen values ('u17', 1, 11, 182.38);

-- u18 Sessions
insert into listen values ('u18', 3, 1, 12.7);
insert into listen values ('u18', 3, 26, 26.8);
insert into listen values ('u18', 3, 17, 23.4);
insert into listen values ('u18', 3, 21, 32);
insert into listen values ('u18', 2, 32, 43.2);
insert into listen values ('u18', 2, 26, 129.5);
insert into listen values ('u18', 1, 26, 45.7);
insert into listen values ('u18', 1, 24, 24.6);

-- u19 Sessions
insert into listen values ('u19', 3, 32, 9.9);
insert into listen values ('u19', 3, 5, 10);
insert into listen values ('u19', 3, 20, 10.1);
insert into listen values ('u19', 3, 19, 15);
insert into listen values ('u19', 3, 14, 8);
insert into listen values ('u19', 1, 24, 34.2);
insert into listen values ('u19', 1, 26, 45);

-- u20 Sessions
insert into listen values ('u20', 1, 23, 3.2);
insert into listen values ('u20', 1, 12, 45);
insert into listen values ('u20', 1, 43, 32);
insert into listen values ('u20', 1, 5, 44);
insert into listen values ('u20', 1, 6, 32);
insert into listen values ('u20', 1, 42, 0.9);

-- u21 Sessions
insert into listen values ('u21', 1, 41, 45.2);
insert into listen values ('u21', 1, 16, 32.6);
insert into listen values ('u21', 1, 32, 5.3);
insert into listen values ('u21', 1, 51, 41);

-- u22 Sessions
insert into listen values ('u22', 2, 40, 23.1);
insert into listen values ('u22', 2, 50, 14.01);
insert into listen values ('u22', 1, 42, 83.46);
insert into listen values ('u22', 1, 11, 29.99);
insert into listen values ('u22', 1, 15, 12.43);
insert into listen values ('u22', 1, 32, 111.11);

-- u23 Sessions
insert into listen values ('u23', 4, 45, 70.3);
insert into listen values ('u23', 4, 33, 67.5);
insert into listen values ('u23', 4, 15, 81);
insert into listen values ('u23', 4, 50, 8);
insert into listen values ('u23', 3, 43, 32);
insert into listen values ('u23', 3, 31, 29);
insert into listen values ('u23', 3, 50, 4);
insert into listen values ('u23', 2, 50, 1);
insert into listen values ('u23', 2, 3, 10.4);
insert into listen values ('u23', 2, 10, 105.7);
insert into listen values ('u23', 2, 21, 12);
insert into listen values ('u23', 2, 36, 11);
insert into listen values ('u23', 2, 37, 20);
insert into listen values ('u23', 2, 41, 11);
insert into listen values ('u23', 1, 1, 15);
insert into listen values ('u23', 1, 50, 1);
insert into listen values ('u23', 1, 8, 4.9);
insert into listen values ('u23', 1, 44, 23);
insert into listen values ('u23', 1, 19, 19);
insert into listen values ('u23', 1, 3, 5);

-- u24 Sessions
insert into listen values ('u24', 2, 44, 39.2);
insert into listen values ('u24', 2, 17, 54.8);
insert into listen values ('u24', 2, 35, 30.4);
insert into listen values ('u24', 2, 36, 23.6);
insert into listen values ('u24', 2, 28, 55.5);
insert into listen values ('u24', 1, 42, 23.5);
insert into listen values ('u24', 1, 11, 32.5);
insert into listen values ('u24', 1, 15, 23.55);
insert into listen values ('u24', 1, 32, 21.3);

-- u25 Sessions
insert into listen values ('u25', 2, 44, 32.6);
insert into listen values ('u25', 2, 17, 40.5);
insert into listen values ('u25', 2, 6, 6.5);
insert into listen values ('u25', 2, 10, 10.9);
insert into listen values ('u25', 2, 18, 23);
insert into listen values ('u25', 1, 4, 345.32);

-- u26 Sessions
insert into listen values ('u26', 2, 44, 32.2);
insert into listen values ('u26', 2, 34, 22);
insert into listen values ('u26', 2, 26, 20);
insert into listen values ('u26', 1, 16, 5);
insert into listen values ('u26', 1, 18, 5.6);
insert into listen values ('u26', 1, 41, 23.2);

-- u27 Sessions
insert into listen values ('u27', 1, 9, 32);
insert into listen values ('u27', 1, 7, 21);
insert into listen values ('u27', 1, 14, 6);

-- u28 Sessions

-- u29 Sessions
insert into listen values ('u29', 2, 45, 8.5);
insert into listen values ('u29', 2, 44, 23);
insert into listen values ('u29', 2, 23, 33);
insert into listen values ('u29', 2, 7, 7);
insert into listen values ('u29', 2, 8, 5);
insert into listen values ('u29', 1, 39, 12.97);
insert into listen values ('u29', 1, 12, 12.77);
insert into listen values ('u29', 1, 40, 49);

-- u30 Sessions
insert into listen values ('u30', 1, 17, 20);
insert into listen values ('u30', 1, 44, 19.3);
insert into listen values ('u30', 1, 34, 43);
insert into listen values ('u30', 1, 5, 5);
insert into listen values ('u30', 1, 29, 11);

-- u31 Sessions
insert into listen values ('u31', 1, 33, 15.6);
insert into listen values ('u31', 1, 8, 4.3);
insert into listen values ('u31', 1, 15, 3.5);

-- u32 Sessions
insert into listen values ('u32', 4, 42, 4.3);
insert into listen values ('u32', 4, 27, 5.5);
insert into listen values ('u32', 4, 16, 6.4);
insert into listen values ('u32', 4, 5, 4.4);
insert into listen values ('u32', 3, 20, 123);
insert into listen values ('u32', 3, 42, 11.2);
insert into listen values ('u32', 3, 5, 7.6);
insert into listen values ('u32', 1, 4, 501);

-- u33 Sessions
insert into listen values ('u33', 1, 5, 11);
insert into listen values ('u33', 1, 44, 5.5);
insert into listen values ('u33', 1, 20, 11);

-- u34 Sessions
insert into listen values ('u34', 1, 8, 5.1);
insert into listen values ('u34', 1, 9, 9.7);
insert into listen values ('u34', 1, 33, 21.4);
insert into listen values ('u34', 1, 50, 33.5);

-- u35 Sessions
insert into listen values ('u35', 1, 45, 54);
insert into listen values ('u35', 1, 32, 29);
insert into listen values ('u35', 1, 44, 20);
insert into listen values ('u35', 1, 5, 5.3);
insert into listen values ('u35', 1, 4, 32);

-- u36 Sessions
insert into listen values ('u36', 1, 25, 1000);
insert into listen values ('u36', 1, 42, 53.6);
insert into listen values ('u36', 1, 9, 43);

-- u37 Sessions
insert into listen values ('u37', 2, 25, 2.6);
insert into listen values ('u37', 2, 35, 10.6);
insert into listen values ('u37', 2, 17, 39.4);
insert into listen values ('u37', 2, 51, 23.3);
insert into listen values ('u37', 2, 31, 19.2);
insert into listen values ('u37', 2, 29, 18);
insert into listen values ('u37', 2, 28, 19);
insert into listen values ('u37', 1, 36, 125);
insert into listen values ('u37', 1, 12, 33.36);

-- u38 Sessions
insert into listen values ('u38', 2, 19, 6);
insert into listen values ('u38', 2, 33, 19.3);
insert into listen values ('u38', 2, 2, 10.5);
insert into listen values ('u38', 2, 8, 20.4);
insert into listen values ('u38', 2, 50, 33.4);
insert into listen values ('u38', 2, 49, 23);
insert into listen values ('u38', 1, 25, 286.21);
insert into listen values ('u38', 1, 51, 59.3);
insert into listen values ('u38', 1, 49, 22);

-- u39 Sessions
insert into listen values ('u39', 2, 29, 2.5);
insert into listen values ('u39', 2, 12, 43);
insert into listen values ('u39', 2, 6, 6);
insert into listen values ('u39', 2, 34, 31);
insert into listen values ('u39', 2, 11, 43);
insert into listen values ('u39', 2, 7, 6);
insert into listen values ('u39', 1, 44, 26.8);
insert into listen values ('u39', 1, 17, 17.9);
insert into listen values ('u39', 1, 29, 43.7);
insert into listen values ('u39', 1, 28, 71.4);
insert into listen values ('u39', 1, 27, 55);

-- u40 Sessions
insert into listen values ('u40', 1, 17, 32);
insert into listen values ('u40', 1, 23, 12);
insert into listen values ('u40', 1, 7, 12.5);
insert into listen values ('u40', 1, 49, 46);

-- u41 Sessions
insert into listen values ('u41', 2, 36, 22.6);
insert into listen values ('u41', 2, 41, 0.3);
insert into listen values ('u41', 2, 38, 5);
insert into listen values ('u41', 1, 37, 43.2);
insert into listen values ('u41', 1, 15, 32);

-- u42 Sessions
insert into listen values ('u42', 3, 29, 10);
insert into listen values ('u42', 3, 11, 15);
insert into listen values ('u42', 2, 33, 33.3);
insert into listen values ('u42', 2, 25, 19);
insert into listen values ('u42', 2, 8, 8.6);
insert into listen values ('u42', 1, 4, 104.18);
insert into listen values ('u42', 1, 9, 23);
insert into listen values ('u42', 1, 6, 24);
insert into listen values ('u42', 1, 43, 15);
insert into listen values ('u42', 1, 3, 14);
insert into listen values ('u42', 1, 41, 41.2);
insert into listen values ('u42', 1, 18, 19.91);
    '''
    
    insert_playlists = '''
insert into playlists values (1, 'Fun Songs', 'u25');
insert into playlists values (2, 'Relaxing Music', 'u40');
insert into playlists values (3, 'Relaxing Music', 'u25');
insert into playlists values (4, '2010s', 'u36');
insert into playlists values (5, 'Pop Music', 'u7');
insert into playlists values (6, 'Obscene Language', 'u11');
insert into playlists values (7, 'Yolo', 'u13');
insert into playlists values (8, 'Favorites', 'u22');
insert into playlists values (9, 'Favorites', 'u22');
insert into playlists values (10, 'Wouldn`t Play Again', 'u33');
insert into playlists values (11, 'Fun Songs', 'u9');
insert into playlists values (12, 'Love These Songs!', 'u34');
insert into playlists values (13, 'Retro Music', 'u22');
insert into playlists values (14, 'Trending Songs', 'u19');
insert into playlists values (15, 'Castle Music', 'u6');
insert into playlists values (16, 'Lady Gaga', 'u17');
insert into playlists values (17, 'Sean Paul', 'u19');
insert into playlists values (18, 'Rap', 'u38');
insert into playlists values (19, 'Pop Music', 'u31');
insert into playlists values (20, 'Let`s Get It!', 'u3');
insert into playlists values (21, 'Funny Songs', 'u27');
insert into playlists values (22, 'Great', 'u24');
insert into playlists values (23, '2013 Songs', 'u26');
insert into playlists values (24, '3 Minute Songs', 'u42');
insert into playlists values (25, '30', 'u28');
insert into playlists values (26, 'Whoa', 'u9');
insert into playlists values (27, 'Lol', 'u15');
insert into playlists values (28, 'Davood`s Favorites', 'u10');
insert into playlists values (29, 'Ryder`s Favorites', 'u12');
insert into playlists values (30, 'Songs for 291', 'u10');
insert into playlists values (31, 'Cool Playlist', 'u18');
insert into playlists values (32, 'Give Me Everything', 'u26');
insert into playlists values (33, 'Blinding', 'u10');
insert into playlists values (34, 'Peaches', 'a56');
insert into playlists values (35, 'Empty Playlist', 'a56');
    '''
    
    insert_plinclude = '''
    -- Playlist 1
insert into plinclude values (1, 35, 1);
insert into plinclude values (1, 24, 3);
insert into plinclude values (1, 9, 2);
insert into plinclude values (1, 42, 4);
insert into plinclude values (1, 25, 5);

-- Playlist 2
insert into plinclude values (2, 8, 1);
insert into plinclude values (2, 5, 2);
insert into plinclude values (2, 15, 3);
insert into plinclude values (2, 17, 4);
insert into plinclude values (2, 19, 5);
insert into plinclude values (2, 39, 6);

-- Playlist 3
insert into plinclude values (3, 5, 1);
insert into plinclude values (3, 42, 2);
insert into plinclude values (3, 43, 3);
insert into plinclude values (3, 4, 4);
insert into plinclude values (3, 13, 5);
insert into plinclude values (3, 40, 6);

-- Playlist 4
insert into plinclude values (4, 26, 1);
insert into plinclude values (4, 19, 2);
insert into plinclude values (4, 3, 3);

-- Playlist 5
insert into plinclude values (5, 11, 1);
insert into plinclude values (5, 29, 2);
insert into plinclude values (5, 34, 3);
insert into plinclude values (5, 44, 4);

-- Playlist 6
insert into plinclude values (6, 42, 1);
insert into plinclude values (6, 23, 2);
insert into plinclude values (6, 12, 3);
insert into plinclude values (6, 2, 4);
insert into plinclude values (6, 11, 5);
insert into plinclude values (6, 35, 6);
insert into plinclude values (6, 25, 7);
insert into plinclude values (6, 6, 8);
insert into plinclude values (6, 33, 9);

-- Playlist 7
insert into plinclude values (7, 31, 1);
insert into plinclude values (7, 22, 2);
insert into plinclude values (7, 13, 3);
insert into plinclude values (7, 45, 5);
insert into plinclude values (7, 27, 4);

-- Playlist 8
insert into plinclude values (8, 25, 1);
insert into plinclude values (8, 11, 2);

-- Playlist 9
insert into plinclude values (9, 41, 1);
insert into plinclude values (9, 23, 2);
insert into plinclude values (9, 16, 3);
insert into plinclude values (9, 32, 4);
insert into plinclude values (9, 10, 5);
insert into plinclude values (9, 18, 6);
insert into plinclude values (9, 25, 7);
insert into plinclude values (9, 33, 8);
insert into plinclude values (9, 8, 9);
insert into plinclude values (9, 9, 10);

-- Playlist 10
insert into plinclude values (10, 39, 1);
insert into plinclude values (10, 40, 2);
insert into plinclude values (10, 36, 3);
insert into plinclude values (10, 26, 4);
insert into plinclude values (10, 11, 5);
insert into plinclude values (10, 42, 6);
insert into plinclude values (10, 15, 7);

-- Playlist 11
insert into plinclude values (11, 8, 1);
insert into plinclude values (11, 15, 2);
insert into plinclude values (11, 13, 3);
insert into plinclude values (11, 44, 4);
insert into plinclude values (11, 20, 5);
insert into plinclude values (11, 5, 6);
insert into plinclude values (11, 27, 7);
insert into plinclude values (11, 16, 8);
insert into plinclude values (11, 38, 9);
insert into plinclude values (11, 30, 10);
insert into plinclude values (11, 23, 11);

-- Playlist 12
insert into plinclude values (12, 28, 1);
insert into plinclude values (12, 20, 2);
insert into plinclude values (12, 43, 3);

-- Playlist 14
insert into plinclude values (14, 39, 1);
insert into plinclude values (14, 20, 2);
insert into plinclude values (14, 24, 3);
insert into plinclude values (14, 27, 4);

-- Playlist 15
insert into plinclude values (15, 10, 1);
insert into plinclude values (15, 2, 2);
insert into plinclude values (15, 35, 3);

-- Playlist 16
insert into plinclude values (16, 2, 1);
insert into plinclude values (16, 13, 2);
insert into plinclude values (16, 10, 3);
insert into plinclude values (16, 14, 4);
insert into plinclude values (16, 9, 5);
insert into plinclude values (16, 29, 6);
insert into plinclude values (16, 33, 7);
insert into plinclude values (16, 20, 8);
insert into plinclude values (16, 1, 9);
insert into plinclude values (16, 40, 10);

-- Playlist 17
insert into plinclude values (17, 45, 1);
insert into plinclude values (17, 35, 2);
insert into plinclude values (17, 17, 3);
insert into plinclude values (17, 31, 4);
insert into plinclude values (17, 29, 5);
insert into plinclude values (17, 44, 6);
insert into plinclude values (17, 34, 7);
insert into plinclude values (17, 1, 8);
insert into plinclude values (17, 26, 9);
insert into plinclude values (17, 23, 10);
insert into plinclude values (17, 8, 11);
insert into plinclude values (17, 2, 12);
insert into plinclude values (17, 43, 13);
insert into plinclude values (17, 36, 14);
insert into plinclude values (17, 37, 15);
insert into plinclude values (17, 22, 16);
insert into plinclude values (17, 7, 17);

-- Playlist 18
insert into plinclude values (18, 44, 1);
insert into plinclude values (18, 41, 2);

-- Playlist 19
insert into plinclude values (19, 40, 1);
insert into plinclude values (19, 16, 2);
insert into plinclude values (19, 18, 3);
insert into plinclude values (19, 5, 4);
insert into plinclude values (19, 9, 5);
insert into plinclude values (19, 7, 6);
insert into plinclude values (19, 20, 7);

-- Playlist 20
insert into plinclude values (20, 8, 1);
insert into plinclude values (20, 2, 2);
insert into plinclude values (20, 6, 3);

-- Playlist 21
insert into plinclude values (21, 1, 1);
insert into plinclude values (21, 2, 2);
insert into plinclude values (21, 3, 3);
insert into plinclude values (21, 4, 4);
insert into plinclude values (21, 5, 5);
insert into plinclude values (21, 6, 6);
insert into plinclude values (21, 7, 7);
insert into plinclude values (21, 8, 8);
insert into plinclude values (21, 9, 9);
insert into plinclude values (21, 10, 10);
insert into plinclude values (21, 11, 11);
insert into plinclude values (21, 12, 12);
insert into plinclude values (21, 13, 13);
insert into plinclude values (21, 14, 14);
insert into plinclude values (21, 15, 15);
insert into plinclude values (21, 16, 16);
insert into plinclude values (21, 17, 17);
insert into plinclude values (21, 18, 18);
insert into plinclude values (21, 19, 19);
insert into plinclude values (21, 20, 20);
insert into plinclude values (21, 21, 21);
insert into plinclude values (21, 22, 22);
insert into plinclude values (21, 23, 23);
insert into plinclude values (21, 24, 24);
insert into plinclude values (21, 25, 25);
insert into plinclude values (21, 26, 26);
insert into plinclude values (21, 27, 27);
insert into plinclude values (21, 28, 28);
insert into plinclude values (21, 29, 29);
insert into plinclude values (21, 30, 30);
insert into plinclude values (21, 31, 31);
insert into plinclude values (21, 32, 32);
insert into plinclude values (21, 33, 33);
insert into plinclude values (21, 34, 34);
insert into plinclude values (21, 35, 35);
insert into plinclude values (21, 36, 36);
insert into plinclude values (21, 37, 37);
insert into plinclude values (21, 38, 38);
insert into plinclude values (21, 39, 39);
insert into plinclude values (21, 40, 40);
insert into plinclude values (21, 41, 41);
insert into plinclude values (21, 42, 42);
insert into plinclude values (21, 43, 43);
insert into plinclude values (21, 44, 44);
insert into plinclude values (21, 45, 45);

-- Playlist 22
insert into plinclude values (22, 45, 1);
insert into plinclude values (22, 28, 2);

-- Playlist 23
insert into plinclude values (23, 9, 1);
insert into plinclude values (23, 18, 2);

-- Playlist 24
insert into plinclude values (24, 38, 1);

-- Playlist 25
insert into plinclude values (25, 32, 1);
insert into plinclude values (25, 22, 2);
insert into plinclude values (25, 31, 3);
insert into plinclude values (25, 43, 4);
insert into plinclude values (25, 33, 5);
insert into plinclude values (25, 25, 6);
insert into plinclude values (25, 8, 7);

-- Playlist 26
insert into plinclude values (26, 10, 1);
insert into plinclude values (26, 9, 2);
insert into plinclude values (26, 8, 3);
insert into plinclude values (26, 7, 4);

-- Playlist 27
insert into plinclude values (27, 16, 1);
insert into plinclude values (27, 5, 2);
insert into plinclude values (27, 4, 3);
insert into plinclude values (27, 41, 4);
insert into plinclude values (27, 12, 5);
insert into plinclude values (27, 23, 6);

-- Playlist 28
insert into plinclude values (28, 20, 1);
insert into plinclude values (28, 21, 2);
insert into plinclude values (28, 46, 3);

-- Playlist 29
insert into plinclude values (29, 1, 1);
insert into plinclude values (29, 8, 2);
insert into plinclude values (29, 19, 3);
insert into plinclude values (29, 15, 4);
insert into plinclude values (29, 14, 5);

-- Playlist 30
insert into plinclude values (30, 10, 1);
insert into plinclude values (30, 11, 2);
insert into plinclude values (30, 20, 3);
insert into plinclude values (30, 6, 4);
insert into plinclude values (30, 5, 5);
insert into plinclude values (30, 19, 6);
insert into plinclude values (30, 28, 7);
insert into plinclude values (30, 39, 8);
insert into plinclude values (30, 15, 9);
insert into plinclude values (30, 24, 10);
insert into plinclude values (30, 33, 11);
insert into plinclude values (30, 22, 12);
insert into plinclude values (30, 32, 13);
insert into plinclude values (30, 44, 14);
insert into plinclude values (30, 36, 15);
insert into plinclude values (30, 18, 16);
insert into plinclude values (30, 3, 17);
insert into plinclude values (30, 42, 18);
insert into plinclude values (30, 25, 19);
insert into plinclude values (30, 41, 20);
insert into plinclude values (30, 35, 21);
insert into plinclude values (30, 14, 22);
insert into plinclude values (30, 38, 23);

-- Playlist 31
insert into plinclude values (31, 5, 1);
insert into plinclude values (31, 11, 2);
insert into plinclude values (31, 42, 3);
insert into plinclude values (31, 6, 4);
insert into plinclude values (31, 43, 5);
insert into plinclude values (31, 23, 6);
insert into plinclude values (31, 12, 7);
insert into plinclude values (31, 25, 8);
insert into plinclude values (31, 16, 9);
insert into plinclude values (31, 46, 10);

-- Playlist 32
insert into plinclude values (32, 27, 1);
insert into plinclude values (32, 25, 2);
insert into plinclude values (32, 44, 3);

-- Playlist 33
insert into plinclude values (33, 42, 1);
insert into plinclude values (33, 43, 2);
insert into plinclude values (33, 50, 3);
insert into plinclude values (33, 51, 4);

-- Playlist 34
insert into plinclude values (34, 49, 1);
insert into plinclude values (34, 32, 2);
insert into plinclude values (34, 51, 3);
    '''

    
    insert_perform = '''
insert into perform values ('a1', 2);
insert into perform values ('a1', 19);
insert into perform values ('a2', 4);
insert into perform values ('a3', 3);
insert into perform values ('a4', 22);
insert into perform values ('a5', 6);
insert into perform values ('a6', 6);
insert into perform values ('a7', 7);
insert into perform values ('a8', 8);
insert into perform values ('a9', 9);
insert into perform values ('a10', 5);
insert into perform values ('a11', 12);
insert into perform values ('a11', 27);
insert into perform values ('a11', 31);
insert into perform values ('a11', 38);
insert into perform values ('a11', 40);
insert into perform values ('a12', 13);
insert into perform values ('a12', 20);
insert into perform values ('a12', 23);
insert into perform values ('a13', 14);
insert into perform values ('a14', 15);
insert into perform values ('a15', 16);
insert into perform values ('a15', 17);
insert into perform values ('a15', 26);
insert into perform values ('a16', 17);
insert into perform values ('a16', 34);
insert into perform values ('a17', 18);
insert into perform values ('a18', 20);
insert into perform values ('a18', 21);
insert into perform values ('a19', 23);
insert into perform values ('a19', 46);
insert into perform values ('a20', 10);
insert into perform values ('a20', 11);
insert into perform values ('a21', 24);
insert into perform values ('a22', 25);
insert into perform values ('a23', 28);
insert into perform values ('a24', 29);
insert into perform values ('a25', 30);
insert into perform values ('a26', 32);
insert into perform values ('a27', 33);
insert into perform values ('a28', 35);
insert into perform values ('a29', 36);
insert into perform values ('a30', 37);
insert into perform values ('a31', 39);
insert into perform values ('a32', 40);
insert into perform values ('a33', 1);
insert into perform values ('a34', 41);
insert into perform values ('a34', 42);
insert into perform values ('a35', 43);
insert into perform values ('a35', 44);
insert into perform values ('a36', 45);
insert into perform values ('a37', 13);
insert into perform values ('a37', 46);
insert into perform values ('a38', 47);
insert into perform values ('a39', 48);
insert into perform values ('a40', 49);
insert into perform values ('a41', 50);
insert into perform values ('a42', 50);
insert into perform values ('a43', 1);
insert into perform values ('a44', 9);
insert into perform values ('a44', 38);
insert into perform values ('a45', 12);
insert into perform values ('a46', 15);
insert into perform values ('a47', 16);
insert into perform values ('a48', 21);
insert into perform values ('a49', 26);
insert into perform values ('a50', 27);
insert into perform values ('a51', 27);
insert into perform values ('a52', 27);
insert into perform values ('a53', 31);
insert into perform values ('a54', 32);
insert into perform values ('a55', 39);
insert into perform values ('a56', 51);
insert into perform values ('a57', 51);
insert into perform values ('a58', 51);
    '''
    
    insert_artists = '''
    insert into artists values ('a1', 'Lady Gaga', 'United States', 'p4oktf3f9');
insert into artists values ('a2', 'OneRepublic', 'United States', '39kfpe3k9');
insert into artists values ('a3', 'Imagine Dragons', 'United States', 'e3f3kir3t9');
insert into artists values ('a4', 'PSY', 'South Korea', 'opkr3p4iri23');
insert into artists values ('a5', 'P!nk', 'American', 'Hell349495');
insert into artists values ('a6', 'Nate Reuss', 'American', 'eptiitE3?');
insert into artists values ('a7', 'Kelly Clarkson', 'United States', 'TEKkfgjw2#4?');
insert into artists values ('a8', 'Janelle Monáe', 'United States', 'rif3Ftkiq');
insert into artists values ('a9', 'Maroon 5', 'United States', 'efm3if%4l!');
insert into artists values ('a10', 'Drake', 'Canada', 'eriefg0953');
insert into artists values ('a11', 'Pitbull', 'American', 'wporki2p45');
insert into artists values ('a12', 'Sia', 'Australian', 'epk5932bf');
insert into artists values ('a13', 'Neon Trees', 'American', 'eroktOi64');
insert into artists values ('a14', 'Carly Rae Jepsen', 'Canada', '!2remtf35');
insert into artists values ('a15', 'Calvin Harris', 'Scotland', 'w4eikt3');
insert into artists values ('a16', 'Ellie Goulding', 'United Kingdom', 'po5oE5');
insert into artists values ('a17', 'Avicii', 'Swedish', 'lLgtk34');
insert into artists values ('a18', 'Sean Paul', 'Jamaica', 'lremgp@r4kt');
insert into artists values ('a19', 'David Guetta', 'French', 'erkgtY542');
insert into artists values ('a20', 'Bob Ezrin', 'Canadian', 'lkeoito53$35fF');
insert into artists values ('a21', 'Echosmith', 'American', 'kefi3emrio');
insert into artists values ('a22', 'The Wanted', 'British', 'wkfop3rf95');
insert into artists values ('a23', 'Selena Gomez', 'United States', 'egfpe5762');
insert into artists values ('a24', 'Rixton', 'British', 'kemT6453');
insert into artists values ('a25', 'American Authors', 'American', 'mogemity4Tr');
insert into artists values ('a26', 'Cobra Starship', 'American', 'kt45t965&');
insert into artists values ('a27', 'Captial Cities', 'American', 'lO3pit51');
insert into artists values ('a28', 'WALK THE MOON', 'United States', 'LFerktgip23');
insert into artists values ('a29', 'Jason Derulo', 'American', 'KGeignieort');
insert into artists values ('a30', 'Taio Cruz', 'English', 'erfmitTyker');
insert into artists values ('a31', 'The Script', 'Ireland', 'fermti23');
insert into artists values ('a32', 'Jennifer Lopez', 'American', 'woToi623');
insert into artists values ('a33', 'Shakira', 'Colombia', 'egper9542');
insert into artists values ('a34', 'The Weeknd', 'Canada', 'Re435t21');
insert into artists values ('a35', 'Celine Dion', 'Canada', 'Krgrwe45');
insert into artists values ('a36', 'Avril Lavigne', 'Canadian', 'FLoti424');
insert into artists values ('a37', 'Flo Rida', 'American', 'fegotryi64');
insert into artists values ('a38', 'Spice Girls', 'British', '??23r3t3');
insert into artists values ('a39', 'Ed Sheeran', 'England', 'wgegt53');
insert into artists values ('a40', 'Bad Company', 'England', 'rifi3ojf35');
insert into artists values ('a41', 'Kendrick Lamar', 'American', 'gote');
insert into artists values ('a42', 'Taylor Swift', 'uNitEd StAtes', '4923KFse');
insert into artists values ('a43', 'Freshlyground', 'South Africa', 'reiofjero');
insert into artists values ('a44', 'Christina Aguilera', 'American', 'ejf3ot48');
insert into artists values ('a45', 'Usher', 'AmErIcan', 'f3io4f34i');
insert into artists values ('a46', 'Owl City', 'AMERICAN', '3lntf3');
insert into artists values ('a47', 'John Newman', 'EnGLiSh', '4yh6iiwe');
insert into artists values ('a48', 'Dua Lipa', 'EngLANd', '56zfefenget');
insert into artists values ('a49', 'Rihanna', 'Barbados', 'opejgferti');
insert into artists values ('a50', 'Ne-Yo', 'American', 'porpgv412');
insert into artists values ('a51', 'Afrojack', 'NetherLands', 'bmelrfe');
insert into artists values ('a52', 'Nayer', 'American', '?eg5tg4');
insert into artists values ('a53', 'Chris Brown', 'AMerican', 'mare4');
insert into artists values ('a54', 'Sabi', 'american', 'p23r43');
insert into artists values ('a55', 'will.i.am', 'AmeriCan', '43gffg');
insert into artists values ('a56', 'Justin Bieber', 'CaNAdA', 'epgj4rt');
insert into artists values ('a57', 'Daniel Caesar', 'CaNadian', 'feo53r9');
insert into artists values ('a58', 'Giveon', 'American', 'f34rf3');
insert into artists values ('a59', 'Enrique Iglesias', 'Spanish', 'ppre3');
    '''
    
    cursor.executescript(insert_users)
    cursor.executescript(insert_songs)
    cursor.executescript(insert_sessions)
    cursor.executescript(insert_plinclude)
    cursor.executescript(insert_playlists)
    cursor.executescript(insert_artists)
    cursor.executescript(insert_perform)
    cursor.executescript(insert_listen)
    connection.commit()
    return
    


def main():
    global connection, cursor

    connectDB(DBPath)

    drop_tables()

    create_tables()

    insert_data()

    login_function()
    
    connection.commit()
    connection.close()
    return
    
    

if __name__ == "__main__":
    main()
