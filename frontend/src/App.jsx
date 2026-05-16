import { useState } from 'react';
import UploadSection from './components/UploadSection';
import ResultsDashboard from './components/ResultsDashboard';
import RoadmapTimeline from './components/RoadmapTimeline';

function App() {
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async (resumeFile, jdText) => {
    if (!resumeFile || !jdText) {
      setError("Please provide both a Resume PDF and a Job Description.");
      return;
    }

    setLoading(true);
    setError(null);
    setResults(null);

    const formData = new FormData();
    formData.append('resume', resumeFile);
    formData.append('jd_text', jdText);

    try {
      const response = await fetch(`${import.meta.env.VITE_API_URL}/analyze`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        let errorMsg = `Server error ${response.status}`;
        try {
          const errData = await response.json();
          errorMsg = errData.detail || errorMsg;
        } catch {
          // ignore parsing error
        }
        throw new Error(errorMsg);
      }

      const data = await response.json();
      setResults(data);
    } catch (err) {
      console.error(err);
      setError(`Analysis failed: ${err.message}.`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen py-8 px-4 sm:px-6 lg:px-8">
      <div className="max-w-7xl mx-auto space-y-12">
        {/* Header Section */}
        <div className="text-center animate-fade-in">
          <h1 className="text-4xl md:text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-sky-400 mb-4">
            AI-Adaptive Onboarding Engine
          </h1>
          <p className="text-lg text-slate-400 max-w-2xl mx-auto">
            Analyze candidate resumes against job descriptions, extract skill gaps, and generate personalized learning roadmaps instantly.
          </p>
        </div>

        {/* Upload & JD Section */}
        {!results && (
          <div className="flex justify-center w-full animate-fade-in delay-100">
            <UploadSection onAnalyze={handleAnalyze} isLoading={loading} error={error} />
          </div>
        )}

        {/* Loading Spinner */}
        {loading && (
          <div className="flex flex-col items-center justify-center space-y-4 py-12 animate-fade-in delay-200">
            <div className="w-16 h-16 border-4 border-indigo-500/30 border-t-indigo-500 rounded-full animate-spin"></div>
            <p className="text-indigo-400 font-medium">Analyzing skills and generating roadmap...</p>
          </div>
        )}

        {/* Results Dashboard */}
        {results && !loading && (
          <div className="space-y-8 animate-fade-in delay-200">
            <div className="flex justify-end">
              <button 
                onClick={() => setResults(null)}
                className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded-lg transition-colors border border-slate-700"
              >
                ← Analyze Another Candidate
              </button>
            </div>
            
            <ResultsDashboard data={results} />
            <RoadmapTimeline roadmap={results.roadmap} />
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
