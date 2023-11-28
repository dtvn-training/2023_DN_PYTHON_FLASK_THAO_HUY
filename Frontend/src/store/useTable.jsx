import { useState, useEffect } from "react";

// các trang có thể được hiển thị
const calculateRange = (data, rowsPerPage) => {
  const range = [];
  const num = Math.ceil(data.length / rowsPerPage);
  for (let i = 1; i <= num; i++) {
    range.push(i);
  }
  return range;
}

// cắt 1 phần dữ liệu từ 1 trang dựa trên số trang và số hàng
const sliceData = (data, page, rowsPerPage) => {
  return data.slice((page - 1) * rowsPerPage, page * rowsPerPage)
};

// lưu trữ trang thái
const useTable = (data, page, rowsPerPage) => {
  const [config, setConfig] = useState({ pages: [], pageData: [] });

  useEffect(() => {
    const pages = calculateRange(data, rowsPerPage);
    setConfig({ ...config, pages });

    const pageData = sliceData(data, page, rowsPerPage);
    setConfig({ ...config, pageData });
  }, [data, page, rowsPerPage]);
  return config;
};


export default useTable;
