import collections

class Graph:
    def __init__(self):
        # Menyimpan nama vertex dan memetakannya ke indeks matriks
        self.vertex_to_index = {}
        self.index_to_vertex = []
        self.matrix = []

    def tambah_vertex(self, vertex):
        if vertex in self.vertex_to_index:
            print(f"❌ Vertex '{vertex}' sudah ada.")
            return
        
        # Tambahkan ke pemetaan indeks
        self.vertex_to_index[vertex] = len(self.index_to_vertex)
        self.index_to_vertex.append(vertex)
        
        # Perluas matriks yang sudah ada (tambah kolom baru di setiap baris)
        for row in self.matrix:
            row.append(0)
        
        # Tambahkan baris baru untuk vertex baru
        new_row = [0] * len(self.index_to_vertex)
        self.matrix.append(new_row)
        print(f"✅ Vertex '{vertex}' berhasil ditambahkan.")

    def hapus_vertex(self, vertex):
        if vertex not in self.vertex_to_index:
            print(f"❌ Vertex '{vertex}' tidak ditemukan.")
            return
        
        idx = self.vertex_to_index[vertex]
        
        # Hapus baris dari matriks
        self.matrix.pop(idx)
        
        # Hapus kolom dari setiap baris di matriks
        for row in self.matrix:
            row.pop(idx)
            
        # Hapus dari daftar vertex
        self.index_to_vertex.pop(idx)
        
        # Bangun ulang pemetaan indeks karena posisi berubah
        self.vertex_to_index = {v: i for i, v in enumerate(self.index_to_vertex)}
        print(f"✅ Vertex '{vertex}' berhasil dihapus.")

    def tambah_edge(self, u, v, weight=1):
        if u not in self.vertex_to_index or v not in self.vertex_to_index:
            print("❌ Salah satu atau kedua vertex tidak ditemukan.")
            return
        
        idx_u = self.vertex_to_index[u]
        idx_v = self.vertex_to_index[v]
        
        # Menggunakan Graph Tak Berarah (Undirected Graph)
        self.matrix[idx_u][idx_v] = weight
        self.matrix[idx_v][idx_u] = weight
        print(f"✅ Edge antara '{u}' dan '{v}' berhasil ditambahkan.")

    def hapus_edge(self, u, v):
        if u not in self.vertex_to_index or v not in self.vertex_to_index:
            print("❌ Salah satu atau kedua vertex tidak ditemukan.")
            return
        
        idx_u = self.vertex_to_index[u]
        idx_v = self.vertex_to_index[v]
        
        if self.matrix[idx_u][idx_v] == 0:
            print(f"❌ Tidak ada edge antara '{u}' dan '{v}'.")
            return

        self.matrix[idx_u][idx_v] = 0
        self.matrix[idx_v][idx_u] = 0
        print(f"✅ Edge antara '{u}' dan '{v}' berhasil dihapus.")

    def tampilkan_graph(self):
        if not self.index_to_vertex:
            print("📭 Graph kosong.")
            return
        
        print("\n--- ADJACENCY MATRIX ---")
        # Print header kolom
        print("    ", "  ".join(self.index_to_vertex))
        # Print baris matriks
        for i, row in enumerate(self.matrix):
            print(f"{self.index_to_vertex[i]:<3} {row}")
        print("------------------------")

    def traversal_dfs(self, start_vertex):
        if start_vertex not in self.vertex_to_index:
            print(f"❌ Vertex '{start_vertex}' tidak ditemukan.")
            return
        
        visited = set()
        hasil = []
        
        def dfs_helper(v):
            visited.add(v)
            hasil.append(v)
            idx = self.vertex_to_index[v]
            # Cari tetangga yang terhubung (nilai > 0)
            for i, val in enumerate(self.matrix[idx]):
                if val > 0:
                    tetangga = self.index_to_vertex[i]
                    if tetangga not in visited:
                        dfs_helper(tetangga)

        dfs_helper(start_vertex)
        print(f"➔ Hasil DFS: {' -> '.join(hasil)}")

    def traversal_bfs(self, start_vertex):
        if start_vertex not in self.vertex_to_index:
            print(f"❌ Vertex '{start_vertex}' tidak ditemukan.")
            return
        
        visited = set()
        queue = collections.deque([start_vertex])
        visited.add(start_vertex)
        hasil = []
        
        while queue:
            v = queue.popleft()
            hasil.append(v)
            
            idx = self.vertex_to_index[v]
            for i, val in enumerate(self.matrix[idx]):
                if val > 0:
                    tetangga = self.index_to_vertex[i]
                    if tetangga not in visited:
                        visited.add(tetangga)
                        queue.append(tetangga)
                        
        print(f"➔ Hasil BFS: {' -> '.join(hasil)}")


# --- MAIN PROGRAM MENU ---
def main():
    g = Graph()
    
    while True:
        print("\n================ MENU ================")
        print("1. Tambah Vertex")
        print("2. Hapus Vertex")
        print("3. Tambah Edge")
        print("4. Hapus Edge")
        print("5. Tampilkan graph (Matrix)")
        print("6. Traversal DFS")
        print("7. Traversal BFS")
        print("8. Quit")
        print("======================================")
        
        pilihan = input("Pilih menu (1-8): ").strip()
        
        if pilihan == '1':
            v = input("Masukkan nama Vertex baru: ").strip()
            if v: g.tambah_vertex(v)
            
        elif pilihan == '2':
            v = input("Masukkan nama Vertex yang ingin dihapus: ").strip()
            if v: g.hapus_vertex(v)
            
        elif pilihan == '3':
            u = input("Masukkan Vertex asal: ").strip()
            v = input("Masukkan Vertex tujuan: ").strip()
            if u and v: g.tambah_edge(u, v)
            
        elif pilihan == '4':
            u = input("Masukkan Vertex asal: ").strip()
            v = input("Masukkan Vertex tujuan: ").strip()
            if u and v: g.hapus_edge(u, v)
            
        elif pilihan == '5':
            g.tampilkan_graph()
            
        elif pilihan == '6':
            v = input("Masukkan Vertex awal DFS: ").strip()
            if v: g.traversal_dfs(v)
            
        elif pilihan == '7':
            v = input("Masukkan Vertex awal BFS: ").strip()
            if v: g.traversal_bfs(v)
            
        elif pilihan == '8':
            print("Terima kasih! Keluar dari program.")
            break
        else:
            print("❌ Pilihan tidak valid. Silakan pilih menu 1-8.")

if __name__ == "__main__":
    main()