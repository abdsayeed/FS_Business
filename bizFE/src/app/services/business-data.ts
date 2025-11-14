import { Injectable } from '@angular/core';
import jsonData from '../../assets/businesses.json';

@Injectable({
  providedIn: 'root',
})
export class BusinessData {
  pageSize: number = 3; // 3 businesses per page

  getBusinesses(page: number) {
    const pageStart = (page - 1) * this.pageSize;
    const pageEnd = pageStart + this.pageSize;
    return jsonData.slice(pageStart, pageEnd);
  }

  getLastPageNumber() {
    return Math.ceil(jsonData.length / this.pageSize);
  }
}

getBusiness(id:any){
  let datatoreturn:any[] = [];
  jsonData.forEach(functon(business){
    if(business._id.$oid == id){
      datatoreturn.push(business);
    }
  })
  return datatoreturn;

}