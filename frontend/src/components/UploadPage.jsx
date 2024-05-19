import React, { useState } from "react";
import axios from "axios";
import pdfIcon from "../images/pdf_icon.png";
import uploadBtn from "../images/upload_btn.png";
import logo from "../images/logo.jpg";

const UploadPage = () => {
  // All States
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(false);
  const [uploadFile, setUploadFile] = useState(null);

  // handler method to take file and upload it
  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    setUploadFile(file);

    const formData = new FormData();
    formData.append("file", file);
    setLoading(true);
    try {
      await axios.post(
        `${process.env.REACT_APP_BACKEND_URL}/upload`,
        formData,
        { headers: { "Content-Type": "multipart/form-data" } }
      );
      setLoading(false);
      setError(false);
      alert("Your PDF file has been successfully stored!");
    } catch (error) {
      setLoading(false);
      setError(true);
    }
  };

  // handler for open file uploader clicking on upload button
  const handleFileUpload = () => document.getElementById("fileInput").click()
  
  return (
    <div className="upload-container">
      {/* App logo */}
      <img src={logo} alt="App Logo" />

      <div className="pdf-wrapper">
        {loading ? (
          <p>Loading.....</p>
        ) : error ? (
          <p>Something went wrong.</p>
        ) : (
          uploadFile && (
            <p>
              {/* Name and logo of uploaded file */}
              <img src={pdfIcon} alt="PDF Icon" />
              {uploadFile.name}
            </p>
          )
        )}
        {/* Upload button */}
        <button
          className="upload-btn"
          onClick={handleFileUpload}
        >
          Upload PDF
        </button>
        <button
          className="small"
          onClick={handleFileUpload}
        >
          <img src={uploadBtn} alt="Upload Button" />
        </button>
      </div>
      {/* File Selector */}
      <input
        id="fileInput"
        type="file"
        style={{ display: "none" }}
        accept="application/pdf"
        onChange={handleFileChange}
      />
    </div>
  );
};

export default UploadPage;
