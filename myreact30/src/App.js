import { useState } from 'react';
import TopNav from 'components/TopNav';
import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import PageLotto from 'pages/PageLotto';

function App() {
  const [pageName, setPageName] = useState('about');
  // 클릭할 때마다 페이지 전환하기
  // const changePageName = () => {
  //   setPageName(pageName === 'about' ? 'counter' : 'about');
  // };

  // const changePageName = () => {
  //   setPageName(pageName);
  // };

  return (
    <div>
      <h1>뭉지의 리액트</h1>

      {/* <button onClick={changepageName}>페이지 토글</button> */}
      <TopNav changePageName={setPageName} />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
      {pageName === 'lotto' && <PageLotto />}
    </div>
  ); // initial: Counter의 상태값(stats)
}

export default App;

// 선택적 랜더링 : {조건 && 컴포넌트} - 조건이 참이라면 컴포넌트를 랜더링한다 .
