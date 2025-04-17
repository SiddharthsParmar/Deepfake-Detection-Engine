import React, { useState } from 'react';
import axios from 'axios';

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState('');
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setResult('');
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    try {
      const response = await axios.post("http://localhost:8000/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });
      setResult(`Prediction: ${response.data.result}`);
    } catch (error) {
      setResult("❌ Upload failed. Try again.");
    }
    setLoading(false);
  };

  return (
    <div className="max-w-md mx-auto p-4 mt-10 border border-gray-200 shadow-lg rounded-xl text-center">
      <h1 className="text-2xl font-bold mb-4">🧠 Deepfake Detector</h1>
      <input
        type="file"
        accept="image/*"
        onChange={handleFileChange}
        className="mb-4 block w-full text-sm"
      />
      <button
        onClick={handleUpload}
        disabled={!file || loading}
        className="bg-blue-600 text-white px-6 py-2 rounded hover:bg-blue-700 disabled:opacity-50"
      >
        {loading ? "Processing..." : "Upload & Detect"}
      </button>
      {result && <p className="mt-4 text-lg font-semibold">{result}</p>}
    </div>
  );
};

export default UploadForm;
