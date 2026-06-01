import heapq

# ==============================================================================
# 1. GRAPH DEFINITION (BATAVIA TRAM NETWORK 1934 - CRISIS CONTEXT)
# ==============================================================================
# Format: 'Station_Name': [('Neighbor_Name', distance_km, fare_G), ...]
graph = {
    'Djembatan Lima': [('Asemka', 1.3, 5)],
    'Asemka': [('Djembatan Lima', 1.3, 5), ('Molenvliet', 1.2, 5), ('Jacatraweg', 1.3, 5)],
    'Molenvliet': [('Asemka', 1.2, 5), ('Batavia', 1.2, 5), ('Sawah Besar', 1.6, 5), ('Harmoni', 1.5, 6)],
    'Jacatraweg': [('Asemka', 1.3, 5), ('Pintoe Besi', 2.0, 9)],
    'Batavia': [('Molenvliet', 1.2, 5)],
    'Pintoe Besi': [('Jacatraweg', 2.0, 9), ('Sawah Besar', 1.5, 4), ('Senen', 2.4, 9)],
    'Sawah Besar': [('Molenvliet', 1.6, 5), ('Pintoe Besi', 1.5, 4)],
    'Harmoni': [('Molenvliet', 1.5, 6), ('Rijswijk', 0.8, 3), ('Koningsplein', 1.0, 4), ('Tanah Abang', 2.5, 12)],
    'Rijswijk': [('Harmoni', 0.8, 3), ('Senen', 2.0, 10)],
    'Koningsplein': [('Harmoni', 1.0, 4), ('Menteng', 1.8, 8)],
    'Tanah Abang': [('Harmoni', 2.5, 12), ('Tamarindelaan', 1.5, 7)],
    'Senen': [('Pintoe Besi', 2.4, 9), ('Rijswijk', 2.0, 10), ('Kramat', 1.2, 5)],
    'Kramat': [('Senen', 1.2, 5), ('Menteng', 1.5, 7), ('Matramanweg', 1.5, 13)],
    'Menteng': [('Koningsplein', 1.8, 8), ('Kramat', 1.5, 7), ('Tamarindelaan', 1.2, 3)],
    'Tamarindelaan': [('Menteng', 1.2, 3), ('Tanah Abang', 1.5, 7)],
    'Matramanweg': [('Kramat', 1.5, 13), ('Mr.Cornelis', 3.0, 20)],
    'Mr.Cornelis': [('Matramanweg', 3.0, 20)]
}



# Spatial heuristics h(n) used for User Efficiency dimensions (A* and Greedy BFS)
heuristics = {
    'Batavia': 0.0, 
    'Asemka': 1.5, 
    'Molenvliet': 1.2, 
    'Jacatraweg': 1.3,
    'Djembatan Lima': 3.0, 
    'Harmoni': 3.0, 
    'Sawah Besar': 3.5, 
    'Rijswijk': 2.8,
    'Pintoe Besi': 2.5, 
    'Koningsplein': 4.5, 
    'Senen': 4.2, 
    'Tanah Abang': 5.0,
    'Menteng': 6.5, 
    'Tamarindelaan': 5.5, 
    'Kramat': 5.5, 
    'Matramanweg': 8.0,
    'Mr.Cornelis': 10.5
}



def calculate_metrics(path):
    """Calculates total track distance (km) and total fare revenue (G) for a completed route."""
    total_km = 0.0
    total_g = 0
    for i in range(len(path) - 1):
        for neighbor, km, g in graph[path[i]]:
            if neighbor == path[i+1]:
                total_km += km
                total_g += g
                break
    return round(total_km, 2), total_g

# ==============================================================================
# 2. ALGORITHMS IMPLEMENTATION
# ==============================================================================

def greedy_best_first_search(start, goal):
    pq = [(heuristics[start], start, [start])]
    visited = set()
    expanded = 0
    while pq:
        _, current, path = heapq.heappop(pq)
        if current == goal: return path, expanded
        if current in visited: continue
        visited.add(current)
        expanded += 1
        for neighbor, _, _ in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (heuristics[neighbor], neighbor, path + [neighbor]))
    return None, expanded

def a_star_search(start, goal):
    pq = [(0 + heuristics[start], 0, start, [start])]
    visited = set()
    expanded = 0
    while pq:
        _, cost_km, current, path = heapq.heappop(pq)
        if current == goal: return path, expanded
        if current in visited: continue
        visited.add(current)
        expanded += 1
        for neighbor, km, _ in graph[current]:
            if neighbor not in visited:
                g_next = cost_km + km
                f_next = g_next + heuristics[neighbor]
                heapq.heappush(pq, (f_next, g_next, neighbor, path + [neighbor]))
    return None, expanded

def dijkstra_search(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    expanded = 0
    while pq:
        cost_km, current, path = heapq.heappop(pq)
        if current == goal: return path, expanded
        if current in visited: continue
        visited.add(current)
        expanded += 1
        for neighbor, km, _ in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost_km + km, neighbor, path + [neighbor]))
    return None, expanded

def uniform_cost_search_g(start, goal):
    pq = [(0, start, [start])]
    visited = set()
    expanded = 0
    while pq:
        cost_g, current, path = heapq.heappop(pq)
        if current == goal: return path, expanded
        if current in visited: continue
        visited.add(current)
        expanded += 1
        for neighbor, _, g in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, (cost_g + g, neighbor, path + [neighbor]))
    return None, expanded

def branch_and_bound_survival(start, goal):
    """
    Business/Operator Context (BVM 1934 Crisis):
    Simulates corporate pruning. Tracks how many route proposals are 'pruned' (cut) 
    because they violate the economic efficiency bound during the Great Depression.
    """
    # Priority branching by lowest operational cost
  
            
        # 1934 DEPRESSION BOUND CHECK: 
        # If partial route cost exceeds our best baseline solution, prune it immediately!
        
    # Use heapq instead of list sorting
    pq = [(0, [start])]
    best_cost = float('inf')
    best_path = None
    nodes_expanded = 0
    routes_pruned = 0
    
    while pq:
        cost_g, path = heapq.heappop(pq)
        current = path[-1]
        
        # Pruning check
        if cost_g >= best_cost:
            routes_pruned += 1
            continue
            
        if current == goal:
            best_cost = cost_g
            best_path = path
            continue
            
        nodes_expanded += 1
        for neighbor, _, g in graph[current]:
            if neighbor not in path:
                heapq.heappush(pq, (cost_g + g, path + [neighbor]))
                
    return best_path, nodes_expanded, routes_pruned
# ==============================================================================
# 3. ANALYSIS OUTPUT GENERATION
# ==============================================================================
start, goal = 'Mr.Cornelis', 'Batavia'

print("=" * 95)
print("MATRIKS HASIL KOMPUTASI: OPTIMASI RUTE TREM BATAVIA 1934 MR CORNELIS - BATAVIA (ZAMAN MELESET)")
print("=" * 95)
print(f"{'Algoritma':<26} | {'Dimensi Analisis':<22} | {'Jarak (km)':<12} | {'Tarif (G)':<10} | {'Ekspansi Node'}")
print("-" * 95)

# 1. Run Standard User-side / Commuter-side algorithms
for name, dim, func in [
    ("Greedy Best-First Search", "User (Efisiensi Waktu)", greedy_best_first_search),
    ("A* Search", "User (Efisiensi Waktu)", a_star_search),
    ("Dijkstra Algorithm", "User (Efisiensi Waktu)", dijkstra_search),
    ("Uniform Cost Search", "Commuter (Efisiensi Biaya)", uniform_cost_search_g)
]:
    p, exp = func(start, goal)
    km, g = calculate_metrics(p)
    print(f"{name:<26} | {dim:<22} | {km:<3} km | {g:<2} G | {exp:<3}")

# 2. Run Corporate Branch & Bound with its specific pruning metrics
p_bb, exp_bb, prune_count = branch_and_bound_survival(start, goal)
km_bb, g_bb = calculate_metrics(p_bb)
print(f"{'Branch and Bound':<26} | {'Operasional (BVM Survival)':<22} | {km_bb:<3} km | {g_bb:<2} G | {exp_bb:<3} (Pruned: {prune_count})")
print("=" * 95)

print("\nSTRUKTUR FILOSOFI RUTE:")
p_gbfs, _ = greedy_best_first_search(start, goal)
p_astar, _ = a_star_search(start, goal)
print(f"1. Rute Intuisi Komuter (Greedy BFS) : {' -> '.join(p_gbfs)}")
print(f"2. Rute Terencana Digital (A* / Dij) : {' -> '.join(p_astar)}")
print(f"3. Rute Bertahan Krisis BVM (B&B) : {' -> '.join(p_bb)}")