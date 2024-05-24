import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DateRangeReportsModalComponent } from './date-range-reports-modal.component';

describe('DateRangeReportsModalComponent', () => {
  let component: DateRangeReportsModalComponent;
  let fixture: ComponentFixture<DateRangeReportsModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DateRangeReportsModalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DateRangeReportsModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
