//
// Created by flawreen on 5/31/23.
//
#include <iostream>
using namespace std;
class Node {
public:
	int val;
	Node *left, *right;

	explicit Node(int x) {
		val = x;
		this->left = nullptr;
		this->right = nullptr;
	}
	Node* insert(Node* node, int x) {
		if (node == nullptr) {
			return new Node(x);
		}
		if (x < node->val) {
			node->left = insert(node->left, x);
		} else if (x > node->val) {
			node->right = insert(node->right, x);
		}
		return node;
	}

	void ex1(Node* root, int k, int nivelCurent = 0) {
		if (root == nullptr || nivelCurent > k) {
			return;
		}
		if (nivelCurent == k) {
			cout << root->val << " ";
		}
		ex1(root->left, k, nivelCurent+1);
		ex1(root->right, k, nivelCurent+1);
	}

};



int main() {
	Node *root = nullptr;
	root = root->insert(root, 8);
	root->insert(root, 6);
	root->insert(root, 10);
	root->insert(root, 3);
	root->insert(root, 9);
	root->insert(root, 15);
	root->insert(root, 2);
	root->insert(root, 4);
	root->insert(root, 12);
	/*
0				    8
			  /           \
1      		6  	   	       10
		   /		   /         \
2	      3           9           15
	   /    \                   /
3	  2      4                12

	 */

	root->ex1(root, 1); // 6 10


	return 0;
}

