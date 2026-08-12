import React from 'react';
import { Code, Database, Terminal, Layout } from 'lucide-react';

const SkillBadge = ({ skill }) => {
  const getIcon = (category) => {
    switch (category) {
      case 'frontend': return <Layout size={18} />;
      case 'backend': return <Code size={18} />;
      case 'database': return <Database size={18} />;
      default: return <Terminal size={18} />;
    }
  };

  return (
    <div className="skill-badge">
      {getIcon(skill.category)}
      <span style={{ fontWeight: 500 }}>{skill.name}</span>
      <span style={{ marginLeft: 'auto', color: 'var(--text-secondary)', fontSize: '0.875rem' }}>
        {skill.proficiency}%
      </span>
    </div>
  );
};

export default SkillBadge;
