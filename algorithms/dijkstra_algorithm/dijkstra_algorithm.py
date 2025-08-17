import heapq


def dijkstra(graph, start):
    """
    Алгоритм Дейкстры для поиска кратчайших путей.

    :param graph: Граф в виде словаря {вершина: {сосед: вес}}
    :param start: Начальная вершина
    :return: Словарь с кратчайшими расстояниями
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
