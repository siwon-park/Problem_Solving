// A Sorting Problem (23336번)
import java.util.*;
import java.io.*;

public class Main {
		
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[][] arr = new int[N + 1][2];
		for (int i = 1; i < N + 1; i++) {
			arr[i][0] = Integer.parseInt(st.nextToken());
			arr[i][1] = i;
		}
		
		Arrays.sort(arr, (o1, o2) -> Integer.compare(o1[0], o2[0]));
		
		FenwickTree fenwick = new FenwickTree(N);
		long ans = 0;
		for (int i = 1; i < N + 1; i++) {
			fenwick.update(arr[i][1]);
			ans += fenwick.sum(N) - fenwick.sum(arr[i][1]);
		}
		
		System.out.println(ans);
	}
}

class FenwickTree {
	long[] tree; // N이 최대 20만이기 때문에 swap하면 long
	int size;
	
	FenwickTree(int n) {
		this.tree = new long[n * 4];
		this.size = n;
	}
	
	void update(int i) {
		while (i <= size) {
			tree[i] += 1;
			i += (i & -i);
		}
	}
	
	long sum(int i) {
		long ans = 0;
		while (i > 0) {
			ans += tree[i];
			i -= (i & -i);
		}
		return ans;
	}
}
