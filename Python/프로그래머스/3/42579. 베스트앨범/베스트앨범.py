from collections import defaultdict

def solution(genres, plays):
    answer = []
    music = defaultdict(list)
    total = defaultdict(int) 
    
    for i in range(len(genres)):
        music[genres[i]].append((plays[i], i))
        total[genres[i]] += plays[i]
        
    for genre in music.keys():
        music[genre].sort(key=lambda x: (-x[0], x[1]))
        
    sorted_genres = sorted(total.items(), key=lambda x: -x[1])
    
    for genre, total_play in sorted_genres:
        top_songs = music[genre][:2]
        
        for play, idx in top_songs:
            answer.append(idx)
        
    return answer