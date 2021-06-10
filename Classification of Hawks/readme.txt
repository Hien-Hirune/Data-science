Thông tin chi tiết về tập dữ liệu hawks: https://rdrr.io/cran/Stat2Data/man/Hawks.html

Với mỗi thực nghiệm A-C bên dưới, sử dụng WEKA Explorer để tiến hành phân lớp dữ liệu bằng cách sử dụng các phương pháp phân lớp sau với tham số mặc định: 
  1) NaiveBayesSimple
  2) Id3
  3) J48. 
Với mỗi phương pháp áp dụng trên tập dữ liệu, hãy sử dụng các phương pháp đánh giá sau (xem “Test options” trong cửa số “Classify” của Weka Explorer): 
  a) “Use training set”
  b) “Cross-validation” với 10 fold
  c) “Percentage split” với tỉ lệ 66%. 
  Ghi nhận lại các kết quả của từng lượt chạy vào tập tin Excel “Result.xls”
===-------------------------------------------------===
Các yêu cầu:
  (A) Phân lớp dữ liệu trên tập sử dụng bốn phương pháp phân lớp và từng chiến lược đánh giá đã nêu bên trên.
  (B) Rời rạc hóa mọi thuộc tính không phải là lớp trong tập dữ liệu thành 10 giỏ có độ rộng bằng nhau: sử dụng chức năng “Filter” trong cửa số “Preprocess” của Explorer, chọn ‘filters’ → ‘unsupervised’ → ‘attribute’ → ‘Discretize’. Sử dụng tham số mặc định cho bộ lọc ‘Discretize’. Sau khi đã bảo đảm được mọi thuộc tính không phải lớp đều là rời rạc, thực hiện phân lớp trên tập dữ liệu mới với 3 thuật toán phân lớp và từng chiến lược đánh giá đã nêu bên trên.
  (C) Tiến hành rời rạc hóa mọi thuộc tính không phải là lớp trong tập dữ liệu thành 5 giỏ có độ sâu bằng nhau bằng cách chọn bộ lọc ‘Discretize’ và định tham số thích hợp. Sau khi đã bảo đảm được mọi thuộc tính không phải lớp đều là rời rạc, thực hiện phân lớp trên tập dữ liệu mới với 3 thuật toán phân lớp và từng chiến lược đánh giá đã nêu bên trên.
  (D) Sử dụng WEKA Experimenter. Thực hiện phân lớp dữ liệu sử dụng các phương pháp phân lớp NaiveBayesSimple và J48 với tham số mặc định. Với từng phương pháp
trên tập dữ liệu, chạy 10 lần phương pháp đánh giá cross validation với 10 fold. Ghi nhận lại kết quả vào tập tin “RawResult.csv”. Từ những kết quả này, tính độ chính xác trung bình của mỗi phương pháp cho tập dữ liệu và thêm vào tập tin “Result.xls” (là tập tin trong thực nghiệm A-C) các thông tin sau: 
      a) Thực nghiệm D
      b) Tên của tập dữ liệu
      c) Phương pháp phân lớp
      d) Chiến lược đánh giá
      e) Tỉ lệ trung bình của các mẫu được phân lớp đúng sau 10 × 10 lượt chạy.
  
