import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ListVolunteerComponent } from './list-volunteer.component';

describe('ListVolunteerComponent', () => {
  let component: ListVolunteerComponent;
  let fixture: ComponentFixture<ListVolunteerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ListVolunteerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ListVolunteerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
