import { useState, useRef } from 'react';

export default function UploadSection({ onAnalyze, isLoading, error }) {
  const [file, setFile] = useState(null);
  const [jdText, setJdText] = useState("");
  const fileInputRef = useRef(null);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      const selectedFile = e.target.files[0];
      if (selectedFile.type === "application/pdf") {
        setFile(selectedFile);
      } else {
        alert("Please upload a PDF file.");
      }
    }
  };

  const handleDragOver = (e) => {
    e.preventDefault();
  };

  const handleDrop = (e) => {
    e.preventDefault();
    if (e.dataTransfer.files && e.dataTransfer.files[0]) {
      const droppedFile = e.dataTransfer.files[0];
      if (droppedFile.type === "application/pdf") {
        setFile(droppedFile);
      } else {
        alert("Please upload a PDF file.");
      }
    }
  };

  const handleSubmit = () => {
    onAnalyze(file, jdText);
  };

  return (
    <div className="w-full max-w-4xl space-y-6">
      {error && (
        <div className="bg-red-500/20 border border-red-500/50 text-red-200 p-4 rounded-lg flex items-center space-x-3">
          <svg className="w-5 h-5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clipRule="evenodd" />
          </svg>
          <p>{error}</p>
        </div>
      )}

      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Resume Upload Box */}
        <div 
          className={`glass-panel p-8 flex flex-col items-center justify-center border-2 border-dashed transition-all ${
            file ? 'border-indigo-500 bg-indigo-500/10' : 'border-slate-600 hover:border-slate-500'
          }`}
          onDragOver={handleDragOver}
          onDrop={handleDrop}
          onClick={() => fileInputRef.current?.click()}
        >
          <input 
            type="file" 
            ref={fileInputRef} 
            onChange={handleFileChange} 
            accept="application/pdf"
            className="hidden" 
          />
          
          {file ? (
            <div className="text-center space-y-2">
              <svg className="w-12 h-12 text-indigo-400 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                 <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <p className="text-indigo-300 font-medium">{file.name}</p>
              <p className="text-xs text-slate-400">{(file.size / 1024 / 1024).toFixed(2)} MB</p>
              <button 
                onClick={(e) => { e.stopPropagation(); setFile(null); }}
                className="text-xs text-red-400 hover:text-red-300 mt-2 block w-full"
              >
                Remove
              </button>
            </div>
          ) : (
            <div className="text-center space-y-3 cursor-pointer">
              <div className="bg-slate-800/50 p-4 rounded-full inline-block">
                <svg className="w-8 h-8 text-slate-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                </svg>
              </div>
              <div>
                <p className="text-slate-300 font-medium">Click to upload Resume</p>
                <p className="text-sm text-slate-500">or drag and drop PDF</p>
              </div>
            </div>
          )}
        </div>

        {/* JD Text Area */}
        <div className="glass-panel flex flex-col">
          <div className="px-4 py-3 border-b border-slate-700/50 bg-slate-800/30 rounded-t-xl">
            <h3 className="text-sm font-semibold text-slate-300">Job Description</h3>
          </div>
          <textarea
            value={jdText}
            onChange={(e) => setJdText(e.target.value)}
            placeholder="Paste the target job description here..."
            className="flex-1 w-full p-4 bg-transparent text-slate-300 placeholder-slate-500 resize-none focus:outline-none focus:ring-0"
            style={{ minHeight: '200px' }}
          />
        </div>
      </div>

      <div className="flex justify-center mt-8">
        <button
          onClick={handleSubmit}
          disabled={!file || !jdText || isLoading}
          className={`
            px-8 py-4 rounded-xl font-bold text-lg shadow-lg transition-all
            ${(!file || !jdText || isLoading) 
              ? 'bg-slate-800 text-slate-500 cursor-not-allowed' 
              : 'bg-gradient-to-r from-indigo-600 to-sky-500 hover:from-indigo-500 hover:to-sky-400 text-white hover:-translate-y-1 hover:shadow-indigo-500/25'}
          `}
        >
          {isLoading ? 'Analyzing...' : 'Generate Roadmap'}
        </button>
      </div>
    </div>
  );
}
