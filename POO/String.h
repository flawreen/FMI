#ifndef POO_STRING_H
#define POO_STRING_H

class String {
    char* str;
    int size;

public:
    // Constructori
    String();
    String(const char *s);
    // Constructor de copiere
    String(const String &cpy);
    // Destructor
     ~String();
	// operator= overload pentru copiere
	String& operator= (const String& cpy);
    // operator+ overload pentru concatenare
    String operator+ (const String &a);
    // operator<< overload pentru afisare
    friend std::ostream& operator<<(std::ostream& os, String &str2);
    // operator+= overload pentru adaugarea unei litere la final
    String& operator+= (char s);
    // operator[] pentru gasirea unui subsir
    void operator[] (const char* substr);

};

#endif //POO_STRING_H
