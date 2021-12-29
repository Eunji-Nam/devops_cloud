import ProfileCard from "./components/ProflieCard";
import { useState, useEffect } from "react";
import Axios from "axios";
// import memberProfiles from "./data/ProfileCard.json";
// import PageLotto from "./PageLotto";

function App() {
  const [selectedMemberId, setSelectedMemberId] = useState("bts-jin");
  const [profileList, setProfileList] = useState([]);

  useEffect(() => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        // reponse는 axios 객체
        // response.data => 응답 내용
        setProfileList(response.data);
        console.log(response);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);
  return (
    <>
      {profileList.map((profile, index) => {
        if (selectedMemberId === profile.unique_id) {
          return (
            <div className={`member${(index % 4) + 1}`}>
              <ProfileCard
                {...profile}
                // profileImage={`/image/member${index + 1}.jpg`}
                changePageName={setSelectedMemberId}
              >
                {profileList.map((_profile) => {
                  return (
                    <a
                      onClick={() => setSelectedMemberId(_profile.unique_id)}
                      className={
                        selectedMemberId === _profile.unique_id ? "on" : ""
                      }
                    />
                  );
                })}
              </ProfileCard>
            </div>
          );
        }
      })}
    </>
  );

  // --- react로 ProfileCard 그리기
  // const [selectedMemberId, setSelectedMemberId] = useState(
  //   memberProfiles[0].memberID
  // );

  // return (
  //   <>
  //     {memberProfiles.map((profile, index) => {
  //       if (selectedMemberId === profile.memberID) {
  //         return (
  //           <div className={`member${(index % 4) + 1}`}>
  //             <ProfileCard
  //               {...profile}
  //               profileImage={`/image/member${index + 1}.jpg`}
  //               changePageName={setSelectedMemberId}
  //             >
  //               {memberProfiles.map((_profile) => {
  //                 return (
  //                   <a
  //                     onClick={() => setSelectedMemberId(_profile.memberID)}
  //                     className={
  //                       selectedMemberId === _profile.memberID ? "on" : ""
  //                     }
  //                   />
  //                 );
  //               })}
  //             </ProfileCard>
  //           </div>
  //         );
  //       }
  //     })}
  //   </>
  // );

  // --- 하드코딩으로 ProfileCard 그리기
  // function App() {
  //   const [pageName, setPageName] = useState("DCODELAB");

  //   return (
  //     <div>
  //       {/* <PageLotto /> */}
  //       {pageName === "DCODELAB" && (
  //         <ProfileCard
  //           changePageName={setPageName}
  //           profileImage={<img src={profileImage1} />}
  //           name={"DCODELAB"}
  //           role={"UI/UX INTERACTIVE DEVELOPER"}
  //           facebookUrl={
  //             <a href="https://www.facebook.com/dcodelab80">
  //               facebook.com/dcodelab80
  //             </a>
  //           }
  //           email={"hadaboni80@naver.com"}
  //         />
  //       )}
  //       {pageName === "DOROTHY" && (
  //         <ProfileCard
  //           changePageName={setPageName}
  //           profileImage={<img src={profileImage2} />}
  //           name={"DOROTHY"}
  //           role={"Python"}
  //           facebookUrl={
  //             <a href="https://www.facebook.com/dorothy123">
  //               facebook.com/dorothy123
  //             </a>
  //           }
  //           email={"python123@gmail.com"}
  //         />
  //       )}
  //       {pageName === "JOHN" && (
  //         <ProfileCard
  //           changePageName={setPageName}
  //           profileImage={<img src={profileImage3} />}
  //           name={"JOHN"}
  //           role={"Django"}
  //           facebookUrl={
  //             <a href="https://www.facebook.com/john43">facebook.com/john43</a>
  //           }
  //           email={"django43@kakao.com"}
  //         />
  //       )}
  //       {pageName === "NICK" && (
  //         <ProfileCard
  //           changePageName={setPageName}
  //           profileImage={<img src={profileImage4} />}
  //           name={"NICK"}
  //           role={"react"}
  //           facebookUrl={
  //             <a href="https://www.facebook.com/nick098">facebook.com/nick098</a>
  //           }
  //           email={"react098@nate.com"}
  //         />
  //       )}
  //     </div>
  //   );
}

export default App;
