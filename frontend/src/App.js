import React, { useState } from 'react';
import './App.css';

function App() {
  const [notes, setNotes] = useState('');
  const [task, setTask] = useState('summary');
  const [output, setOutput] = useState('');
  const [loading, setLoading] = useState(false);

  const handleGenerate = async () => {
    if (!notes) return alert("Please enter your class notes.");
    setLoading(true);
    setOutput('');
    try {
      const response = await fetch('http://localhost:5000/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt: notes, task })
      });
      const data = await response.json();
      setOutput(data.result);
    } catch (err) {
      setOutput('Error generating content. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <h1>AI Study Buddy</h1>
      <textarea
        value={notes}
        onChange={(e) => setNotes(e.target.value)}
        placeholder="Paste your class notes here..."
      />
      <select value={task} onChange={(e) => setTask(e.target.value)}>
        <option value="summary">Summary</option>
        <option value="MCQs">MCQs</option>
        <option value="flashcards">Flashcards</option>
        <option value="summary in Bengali">Bengali Summary</option>
      </select>
      <button onClick={handleGenerate}>
        {loading ? 'Generating...' : 'Generate'}
      </button>
      <pre>{output}</pre>
    </div>
  );
}

export default App;
