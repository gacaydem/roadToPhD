# Tản mạn về học thuật toán

Thời gian đầu, tôi bắt đầu bằng việc học khoá Machine Learning của Andrew Ng, như rất nhiều tiền bối đã recommend khi bước chân vào lĩnh vực Data Science. Tuy nhiên, càng học sâu tôi càng thấy kiến thức toán của mình đã bị hổng nhiều. 
Tôi quyết định dừng lại khoá Machine Learning ở week 6 để tập trung lại kiến thức toán qua các khoá Calculus 1A,1B, song song với đó là học khoá Introduction to Computer Science Using Python của MIT. Tại đó, tôi đã được học thuật toán Newton Rhapson, và bỗng chốc, niềm đam mê Toán-Tin bỗng như trỗi dậy, cả thế giới thuật toán như mở ra trước mắt tôi. 
Tôi bắt đầu start khoá Algorithms and Designs của Stanford như một course song song với Calculus.

## Nhận xét

Thuật toán khó. Không dành cho người thiếu kiên nhẫn. Lý thuyết đã khó là vậy, khi hiểu pseudo code và code lại cũng không đơn giản. Recursion quả là 1 phát kiến vĩ đại. Big O notation, oh, my, gosh.

## Các thuật toán đã code

**Karatsuba Interger Multiplication**: một ví dụ kinh điển về việc chứng mình không chỉ có 1 cách giải cho 1 vấn đề đơn giản. Khi code Karatsuba, tôi gặp khó khăn nhiều nhất bởi là script đầu tiên code dạng recursion, nó khá là xoắn não cộng với làm tôi ngộ nhận khá nhiều. Cách đơn giản nhất là lấy 1 ví dụ cực kỳ simple như 12\*12=144, và dùng Karatsuba *nhẩm ra giấy*, ghép lại và đối chiếu. 
Trong quá trình học, tôi tìm ra trang **pythontutor**, quả là một công cụ hay để debug code đặc biệt là recursion

**MergeSort**: deal với MergeSort cũng không đơn giản với người mới, bạn nên def ra 2 tác vụ riêng biệt là merge và sort, merge thì sẽ được sử dụng trong sort. Sort thì sẽ là recursion, tất nhiên rồi. Tôi hoàn thành mergesort trong khoảng 2 tiếng, và quả thật nó quá là hữu ích, tôi chắc recursion như trong lòng bàn tay. *Nhớ trong đầu:* base case là gì, recursion khi nào.

**Selection,Insertion, Bubble Sort**: 3 thuật toán này tôi hoàn thành chỉ trong 1 tiếng do đã nắm khá vững recursion. Kể cả khi đã solve được vấn đề bằng vòng lặp, tôi vẫn thử cố nghĩ xem có cách nào để divide và conquer nó như đã từng làm với merge sort không :v Đáp án tất nhiên là có, nhưng tựu chung lại cũng chẳng làm giảm độ phức tạp của thuật toán đi tí nào. Tôi vui vẻ với việc thay-tất-cả-những-gì-có-thể-thay-được từ loop thành recursion như một bài tập nhỏ cho mình ^^
