import React from 'react';
import './App.css';
import ComboBox from '../src/components/select';
import { SelectInterface } from './common/interfaces';
import { ComboBoxProps } from './common/interfaces';


const top100Films: SelectInterface[] = [
  { en: 'The Shawshank Redemption', rus: 1994 },
  { en: 'The Godfather', rus: 1972 },
  { en: 'The Godfather: Part II', rus: 1974 },
  { en: 'The Dark Knight', rus: 2008 },
  { en: '12 Angry Men', rus: 1957 },
  { en: "Schindler's List", rus: 1993 },
  { en: 'Pulp Fiction', rus: 1994 }
];



function App() {
  return (
    <div className="App">

      <ComboBox 
        words={ top100Films }
        width={100}
      />
    </div>
  );
}

export default App;
