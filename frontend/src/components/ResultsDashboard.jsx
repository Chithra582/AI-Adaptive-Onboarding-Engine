import SkillGaps from './SkillGaps';

export default function ResultsDashboard({ data }) {
  const { resume_analysis, gap_analysis } = data;
  
  const extractedSkills = resume_analysis.extracted_skills || [];

  return (
    <div className="glass-panel p-6 overflow-hidden relative">
      <div className="absolute top-0 right-0 w-64 h-64 bg-indigo-500/10 rounded-full blur-3xl -mr-32 -mt-32 pointer-events-none"></div>
      
      <div className="flex flex-col md:flex-row justify-between items-start md:items-center mb-8 border-b border-white/10 pb-6">
        <div>
          <h2 className="text-2xl font-bold text-white mb-2">Analysis Results</h2>
          <p className="text-slate-400">Match Profile vs Requirements</p>
        </div>
        
        <div className="mt-4 md:mt-0 flex flex-wrap gap-4">
          {/* Match Score */}
          <div className="glass-panel px-6 py-4 flex flex-col bg-slate-900/50 border-emerald-500/20">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">Ready Match</span>
            <span className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-emerald-400 to-cyan-400">
              {gap_analysis.match_percentage}%
            </span>
          </div>

          {/* Resume Score */}
          <div className="glass-panel px-6 py-4 flex flex-col bg-slate-900/50 border-blue-500/20">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">Resume Score</span>
            <span className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-indigo-400">
              {gap_analysis.resume_score}%
            </span>
          </div>

          {/* Projected Score */}
          <div className="glass-panel px-6 py-4 flex flex-col bg-slate-900/50 border-rose-500/20">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">Projected</span>
            <span className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-rose-400 to-amber-400">
              100%
            </span>
          </div>

          {/* Gaps Found Card */}
          <div className="glass-panel px-6 py-4 flex flex-col bg-slate-900/50 border-orange-500/20">
            <span className="text-xs text-slate-400 uppercase tracking-wider block">Gaps Found</span>
            <span className="text-3xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-orange-400 to-amber-400">
              {gap_analysis.missing_skills.length}
            </span>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-10">
        
        {/* Left Col: Extracted info */}
        <div className="space-y-8">
          <div>
            <h3 className="text-lg font-semibold text-indigo-300 mb-4 flex items-center">
              <span className="bg-indigo-500/20 p-1.5 rounded-md mr-2">
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                </svg>
              </span>
              Extracted Profile Skills
            </h3>
            
            <div className="flex flex-wrap gap-2">
              {extractedSkills.length > 0 ? (
                extractedSkills.map((skillItem, idx) => (
                  <div key={idx} className="bg-slate-800/80 border border-slate-700 rounded-full pl-3 pr-2 py-1 text-sm flex items-center space-x-2">
                    <span className="text-slate-200">{skillItem.skill}</span>
                    <span className={`text-[10px] px-1.5 py-0.5 rounded-full ${
                      skillItem.experience_level === 'Advanced' ? 'bg-emerald-500/20 text-emerald-300' :
                      skillItem.experience_level === 'Intermediate' ? 'bg-sky-500/20 text-sky-300' :
                      'bg-slate-500/20 text-slate-300'
                    }`}>
                      {skillItem.experience_level}
                    </span>
                  </div>
                ))
              ) : (
                <p className="text-slate-500 text-sm">No recognizable skills extracted from resume.</p>
              )}
            </div>
          </div>
        </div>

        {/* Right Col: Gap Analysis */}
        <div className="space-y-6">
          <SkillGaps gaps={gap_analysis} />
        </div>

      </div>
    </div>
  );
}
