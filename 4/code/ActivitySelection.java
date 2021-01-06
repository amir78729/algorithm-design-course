import java.util.Scanner;

public class ActivitySelection {
static class Activity{
int r;
int l;
public Activity(int r,int l){
this.l = l;
this.r = r;
}
}

public static Activity[] sort(Activity questions[]){
int n = questions.length;
for(int i = 0; i < n; i++){
for(int j = 0; j < n-1; j++) {
if(questions[j].l > questions[j+1].r) {
Activity tmp = questions[j];
questions[j] = questions[j + 1];
questions[j + 1] = tmp;
}

}

}
// for(int i=0; i< questions.length;i++){
// System.out.println(questions[i].r + " " + questions[i].l);
// }

return questions;
}

public static void checkPossibility(Activity[] questions, int k, int n){
if (questions.length < k){
System.out.println("NO");
return;
}
int count=1;
questions = sort(questions);
for(int i=1; i < questions.length; i++){
// System.out.println(questions[i].r + " " + questions[i-1].l);
if(questions[i].r >= questions[i-1].l || (questions[i].l >= questions[i-1].r && questions[i].r >= questions[i-1].r)){
count++;
}
}

if(count >= n){
System.out.println("YES");
}else{
System.out.println("NO");
}



}

public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int k = sc.nextInt();
Activity[] questions = new Activity[k];
for(int i =0; i < k; i++){
Activity activity = new Activity(sc.nextInt(),sc.nextInt());
questions[i] = activity;
}
checkPossibility(questions,k,n);
}
}