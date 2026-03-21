export default function SkillGaps({ gaps }) {
  const { missing_skills = [], weak_skills = [] } = gaps || {};
  
  return (
    <div className="bg-slate-900/40 rounded-xl p-6 border border-slate-700/50">
      <h3 className="text-lg font-semibold text-rose-300 mb-6 flex items-center">
        <span className="bg-rose-500/20 p-1.5 rounded-md mr-2">
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
          </svg>
        </span>
        Identified Skill Gaps
      </h3>

      <div className="space-y-6">
        {/* Missing Skills */}
        <div>
          <h4 className="text-sm font-medium text-slate-400 mb-3 flex items-center justify-between">
            <span>Critical Missing Skills</span>
            <span className="bg-slate-800 text-xs px-2 py-0.5 rounded-full">{missing_skills?.length || 0}</span>
          </h4>
          
          <div className="flex flex-wrap gap-2">
            {missing_skills && missing_skills.length > 0 ? (
              missing_skills.map((skill, idx) => (
                <span key={idx} className="bg-rose-500/10 border border-rose-500/20 text-rose-300 px-3 py-1 rounded-full text-sm">
                  {skill}
                </span>
              ))
            ) : (
              <p className="text-slate-500 text-sm">No missing skills identified! Great match.</p>
            )}
          </div>
        </div>

        {/* Weak Skills */}
        {weak_skills && weak_skills.length > 0 && (
          <div>
            <h4 className="text-sm font-medium text-slate-400 mb-3 flex items-center justify-between">
              <span>Skills to Strengthen</span>
              <span className="bg-slate-800 text-xs px-2 py-0.5 rounded-full">{weak_skills.length}</span>
            </h4>
            
            <div className="space-y-2">
              {weak_skills.map((ws, idx) => (
                <div key={idx} className="bg-amber-500/10 border border-amber-500/20 rounded-lg p-3">
                  <div className="flex justify-between items-center mb-1">
                    <span className="text-amber-300 font-medium text-sm">{ws.skill}</span>
                    <span className="text-[10px] bg-amber-500/20 text-amber-200 px-2 rounded-full uppercase tracking-wider">
                      Needs Depth
                    </span>
                  </div>
                  <p className="text-xs text-amber-200/70">{ws.reason}</p>
                </div>
              ))}
            </div>
          </div>
        )}

      </div>
    </div>
  );
}
