export default function RoadmapTimeline({ roadmap }) {
  if (!roadmap || roadmap.length === 0) {
    return (
      <div className="glass-panel p-8 text-center text-slate-400">
        <p className="font-medium text-lg text-emerald-400 mb-2">🎉 Candidate is fully qualified!</p>
        <p>No major skill gaps identified. A specialized onboarding path is not required.</p>
      </div>
    );
  }

  return (
    <div className="glass-panel p-8">
      <div className="mb-8">
        <h2 className="text-2xl font-bold text-white mb-2">Targeted Learning Roadmap</h2>
        <p className="text-slate-400">Personalized timeline to bridge identified skill gaps.</p>
      </div>

      <div className="relative border-l-2 border-slate-700/50 ml-3 md:ml-6 space-y-12 pb-4">
        {roadmap.map((step, idx) => (
          <div key={idx} className="relative pl-8 md:pl-10">
            {/* Timeline Dot */}
            <div className={`absolute w-6 h-6 rounded-full -left-[13px] top-1 border-4 border-[#0f172a] shadow-lg flex items-center justify-center
              ${step.type === 'Upskill' ? 'bg-amber-400' : 
                step.type === 'Foundation' ? 'bg-indigo-400' : 'bg-sky-400'}`}
            >
              <div className="w-2 h-2 rounded-full bg-white opacity-50"></div>
            </div>

            {/* Content Card */}
            <div className="bg-slate-800/40 rounded-xl p-5 md:p-6 border border-slate-700/50 hover:bg-slate-800/60 transition-colors group">
              <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-3">
                <div>
                  <div className="flex items-center space-x-3 mb-1">
                    <span className={`text-xs font-bold px-2 py-0.5 rounded-md uppercase tracking-wide
                      ${step.type === 'Upskill' ? 'bg-amber-500/20 text-amber-300' : 
                        step.type === 'Foundation' ? 'bg-indigo-500/20 text-indigo-300' : 'bg-sky-500/20 text-sky-300'}`}
                    >
                      {step.type}
                    </span>
                    <span className="text-sm font-medium text-slate-400">• {step.estimated_time}</span>
                  </div>
                  <h3 className="text-xl font-bold text-white group-hover:text-indigo-300 transition-colors">
                    {step.title}
                  </h3>
                </div>
              </div>
              
              <p className="text-slate-300 text-sm mb-5 leading-relaxed">
                {step.description}
              </p>

              <div>
                <h4 className="text-xs uppercase tracking-wider text-slate-500 mb-2 font-semibold">Suggested Resources</h4>
                <ul className="space-y-1.5 list-disc list-inside">
                  {step.resources.map((res, rIdx) => (
                    <li key={rIdx} className="text-sm text-indigo-200/80 hover:text-indigo-200 transition-colors cursor-pointer">
                      {res}
                    </li>
                  ))}
                </ul>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
